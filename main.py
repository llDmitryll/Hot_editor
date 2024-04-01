import base64
import codecs
import json
import re
import sys

from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt, Slot
from PySide6.QtGui import QFont, QUndoCommand, QUndoStack
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QStyledItemDelegate,
    QStyleOptionViewItem,
    QTableWidgetItem,
    QWidget,
)

import info
from ui_mainwindow import Ui_MainWindow


class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(
        self, parent: QWidget, option: QStyleOptionViewItem, index: QModelIndex | QPersistentModelIndex
    ) -> QWidget:
        return


class TextChangedCommand(QUndoCommand):
    def __init__(self, window: QMainWindow, newitem: QTableWidgetItem | QLineEdit, oldtext: str):
        super().__init__()
        self.newitem = newitem
        self.oldtext = oldtext
        self.newtext = newitem.text()
        self.window = window

    def undo(self) -> None:
        window.reundo = True
        self.newitem.setText(self.oldtext)
        window.reundo = False

    def redo(self) -> None:
        window.reundo = True
        self.newitem.setText(self.newtext)
        window.reundo = False


class MainWindow(QMainWindow):

    def __init__(self, argv: list[str]):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.undoStack = QUndoStack(self)
        self.setWindowTitle("Editor")
        self.file = None
        self.filename = ""
        self.reundo = False
        self.ignore = True
        self.items = 0
        self.data = None
        delegate = ReadOnlyDelegate(self)
        self.statusBar().setFont(QFont("Times", 11))

        self.ui.tableWidget.setItemDelegateForColumn(0, delegate)
        self.undoAction = self.undoStack.createUndoAction(self)
        self.undoAction.setShortcut("Ctrl+Z")
        self.addAction(self.undoAction)
        self.redoAction = self.undoStack.createRedoAction(self)
        self.redoAction.setShortcut("Ctrl+Y")
        self.addAction(self.redoAction)

        self.ui.actionnew.triggered.connect(self.newfile)
        self.ui.actionopen.triggered.connect(self.openfile)
        self.ui.actionsave_as.triggered.connect(self.saveasfile)
        self.ui.actionSave.triggered.connect(self.savefile)
        self.ui.tableWidget.itemChanged.connect(self.datachange)
        self.ui.tableWidget.itemClicked.connect(self.infostat)
        self.ui.nameLineEdit.textEdited.connect(self.named_material)
        self.ui.lineEdit_Y.textEdited.connect(self.named_coordinates)
        self.ui.lineEdit_X.textEdited.connect(self.named_coordinates)
        self.ui.addCoord.clicked.connect(self.add_coordinates)
        self.ui.AddMaterial.clicked.connect(self.add_material)
        self.ui.addImage.clicked.connect(self.add_image)

        if len(argv) == 2:
            self.filename = argv[-1]
            self.openfl()

    @Slot()
    def named_coordinates(self):
        if len(self.ui.lineEdit_X.text()) and len(self.ui.lineEdit_Y.text()) and self.file:
            self.ui.addCoord.setEnabled(True)
        else:
            self.ui.addCoord.setEnabled(False)

    @Slot()
    def add_coordinates(self):
        try:
            float(self.ui.lineEdit_X.text())
            float(self.ui.lineEdit_Y.text())
        except ValueError:
            dialog = QMessageBox(icon=QMessageBox.Icon.Critical, parent=self)
            dialog.setWindowTitle("Error")
            dialog.setText("Coordinates must be real numbers (use . instead of ,)")
            dialog.setFont(QFont("Times", 12))
            self.statusBar().showMessage("ERROR")
            dialog.exec()
            return
        self.data["features"][0]["geometry"]["coordinates"][0] = float(self.ui.lineEdit_X.text())
        self.data["features"][0]["geometry"]["coordinates"][1] = float(self.ui.lineEdit_Y.text())
        self.statusBar().showMessage("Coordinates added")
        self.setWindowTitle(f"Editor {self.filename}*")

    @Slot()
    def named_material(self):
        text = self.ui.nameLineEdit.text()
        if self.file and len(text) != 0:
            self.ui.AddMaterial.setEnabled(True)
        else:
            self.ui.AddMaterial.setEnabled(False)

    @Slot()
    def add_material(self):
        for param in self.ui.material_parametersWidget.findChildren(
            QLineEdit, options=Qt.FindChildOption.FindDirectChildrenOnly
        ):
            if param.text() and not re.match(r"\d+\,?\d*$", param.text()):
                dialog = QMessageBox(icon=QMessageBox.Icon.Critical, parent=self)
                dialog.setWindowTitle("Error")
                dialog.setText('Parameters must be real numbers with ","')
                dialog.setFont(QFont("Times", 12))
                self.statusBar().showMessage("ERROR")
                dialog.exec()
                return
        self.data["features"][0]["Glasses"].clear()
        text = self.ui.nameLineEdit.text()
        self.data["features"][0]["Glasses"].append({text: info.defaultmaterial})
        material = self.data["features"][0]["Glasses"][0][text]
        material["color_RGB"]["Red"] = self.ui.lineEdit_Red.text()
        material["color_RGB"]["Green"] = self.ui.lineEdit_Green.text()
        material["color_RGB"]["Blue"] = self.ui.lineEdit_Blue.text()
        material["roughness"] = self.ui.roughnessLineEdit.text()
        material["transparency"] = self.ui.transparencyLineEdit.text()
        material["metallicity"] = self.ui.metallicityLineEdit.text()
        material["refraction"] = self.ui.refractionLineEdit.text()
        self.setWindowTitle(f"Editor {self.filename}*")
        self.statusBar().showMessage("Material added")

    @Slot()
    def add_image(self):
        file, _ = QFileDialog.getOpenFileName(None, "Open File", "./", "Image 256x256 px (*.jpeg *.jpg *.png)")
        with open(file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            self.ui.tableWidget.setItem(self.items - 2, 1, QTableWidgetItem(str(encoded_string)[2:-1]))
        image_file.close()
        self.statusBar().showMessage("Image added")

    @Slot()
    def infostat(self, item: QTableWidgetItem):
        self.statusBar().showMessage(info.info[self.ui.tableWidget.item(item.row(), 0).text()])

    def openfl(self):
        if self.file:
            self.file.close()
        self.ui.tableWidget.setRowCount(0)
        self.items = 0
        self.ignore = True
        self.file = codecs.open(self.filename, "r", "utf-8-sig")
        self.data = json.load(self.file)
        for key, value in self.data["features"][0]["properties"].items():
            key_item = QTableWidgetItem(key)
            value_item = QTableWidgetItem(value)
            self.ui.tableWidget.insertRow(self.items)
            self.ui.tableWidget.setItem(self.items, 0, key_item)
            self.ui.tableWidget.setItem(self.items, 1, value_item)
            self.items += 1
        self.ignore = False
        if self.data["features"][0]["Glasses"]:
            material = list(self.data["features"][0]["Glasses"][0].values())[0]
            self.ui.nameLineEdit.setText(list(self.data["features"][0]["Glasses"][0].keys())[0])
            self.ui.lineEdit_Red.setText(material["color_RGB"]["Red"])
            self.ui.lineEdit_Green.setText(material["color_RGB"]["Green"])
            self.ui.lineEdit_Blue.setText(material["color_RGB"]["Blue"])
            self.ui.roughnessLineEdit.setText(material["roughness"])
            self.ui.transparencyLineEdit.setText(material["transparency"])
            self.ui.metallicityLineEdit.setText(material["metallicity"])
            self.ui.refractionLineEdit.setText(material["refraction"])
        else:
            self.ui.nameLineEdit.setText("")
            self.ui.lineEdit_Red.setText("")
            self.ui.lineEdit_Green.setText("")
            self.ui.lineEdit_Blue.setText("")
            self.ui.roughnessLineEdit.setText("")
            self.ui.transparencyLineEdit.setText("")
            self.ui.metallicityLineEdit.setText("")
            self.ui.refractionLineEdit.setText("")
        self.ui.lineEdit_X.setText(str(self.data["features"][0]["geometry"]["coordinates"][0]))
        self.ui.lineEdit_Y.setText(str(self.data["features"][0]["geometry"]["coordinates"][1]))
        self.ui.addImage.setEnabled(True)
        self.named_material()
        self.named_coordinates()
        self.setWindowTitle(f"Editor {self.filename}")

    @Slot()
    def newfile(self):
        self.filename, _ = QFileDialog.getSaveFileName(self, "New File", "./", "JSON (*.geojson *.json)")
        file = codecs.open(self.filename, "w", "utf-8-sig")
        file.write(json.dumps(info.clear, indent=4, ensure_ascii=False))
        file.close()
        self.openfl()

    @Slot()
    def openfile(self):
        self.filename, _ = QFileDialog.getOpenFileName(None, "Open File", "./", "JSON (*.geojson *.json)")
        self.openfl()

    @Slot()
    def saveasfile(self):
        self.filename, _ = QFileDialog.getSaveFileName(self, "Save File", "./", "JSON (*.geojson *.json)")
        self.savefile()

    @Slot()
    def savefile(self):
        file = codecs.open(self.filename, "w", "utf-8-sig")
        file.write(json.dumps(self.data, indent=4, ensure_ascii=False))
        file.close()
        self.setWindowTitle(f"Editor {self.filename}")

    @Slot()
    def datachange(self, item: QTableWidgetItem):
        row = item.row()
        if not self.ignore:
            key = self.ui.tableWidget.item(row, 0).text()
            oldtext = self.data["features"][0]["properties"][key]
            self.ignore = True
            item.setText(item.text().replace('"', "'"))
            self.ignore = False
            self.data["features"][0]["properties"][key] = item.text()
            self.setWindowTitle(f"Editor {self.filename}*")
            if not self.reundo:
                command = TextChangedCommand(self, item, oldtext)
                self.undoStack.push(command)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(sys.argv)
    window.show()

    sys.exit(app.exec())