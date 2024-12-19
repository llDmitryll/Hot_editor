import base64
import binascii
import codecs
import json
import re
import sys
import copy
from io import BytesIO

from PIL import Image, UnidentifiedImageError
from PySide6.QtCore import QModelIndex, QPersistentModelIndex, Qt, Slot
from PySide6.QtGui import QCloseEvent, QFont, QUndoCommand, QUndoStack
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QStyledItemDelegate,
    QStyleOptionViewItem,
    QTableWidgetItem,
    QWidget,
    QColorDialog,
    QListWidgetItem,
)

import info
from ui_mainwindow import Ui_MainWindow

VERSION = "v1.0.4"


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
        self.setFont(QFont("Consolas", 9))
        self.setWindowTitle("Editor")
        self.file = None
        self.filename = ""
        self.reundo = False
        self.ignore = True
        self.items = 0
        self.data = None
        self.status_unsaved = ""

        self.undoAction = self.undoStack.createUndoAction(self)
        self.undoAction.setShortcut("Ctrl+Z")
        self.addAction(self.undoAction)
        self.redoAction = self.undoStack.createRedoAction(self)
        self.redoAction.setShortcut("Ctrl+Y")
        self.addAction(self.redoAction)

        self.ui.statusbar.setFont(QFont("Times", 11))
        self.label_Version = QLabel()
        self.label_Version.setStyleSheet("border: 1px solid black;")
        self.label_Version.setText(VERSION)
        self.ui.statusbar.addPermanentWidget(self.label_Version)
        self.delegate = ReadOnlyDelegate(self)
        self.ui.tableWidget.setItemDelegateForColumn(0, self.delegate)
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
        self.ui.deleteMaterial.clicked.connect(self.delete_material)
        self.ui.addMaterial.clicked.connect(self.add_material)
        self.ui.materialsListWidget.itemClicked.connect(self.select_material)
        self.ui.addImage.clicked.connect(self.add_image)
        self.ui.showImage.clicked.connect(self.show_image)
        self.ui.selectColor.clicked.connect(self.select_color)

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
            self.statusBar().showMessage("ERROR")
            dialog.exec()
            return
        self.data["features"][0]["geometry"]["coordinates"][0] = float(self.ui.lineEdit_X.text())
        self.data["features"][0]["geometry"]["coordinates"][1] = float(self.ui.lineEdit_Y.text())
        self.statusBar().showMessage("Coordinates added")
        self.status_unsaved = "*"
        self.setTitle()

    @Slot()
    def select_color(self):
        options = QColorDialog.ColorDialogOption.ShowAlphaChannel
        color = QColorDialog.getColor(parent=self, options=options)
        r, g, b, a = color.getRgb()
        self.ui.lineEdit_Red.setText(str(r))
        self.ui.lineEdit_Green.setText(str(g))
        self.ui.lineEdit_Blue.setText(str(b))

    def fill_material_ui(self, material_dict):
        material = list(material_dict.values())[0]
        self.ui.nameLineEdit.setText(list(material_dict.keys())[0])
        self.ui.lineEdit_Red.setText(material["color_RGB"]["Red"])
        self.ui.lineEdit_Green.setText(material["color_RGB"]["Green"])
        self.ui.lineEdit_Blue.setText(material["color_RGB"]["Blue"])
        self.ui.roughnessLineEdit.setText(material["roughness"])
        self.ui.transparencyLineEdit.setText(material["transparency"])
        self.ui.metallicityLineEdit.setText(material["metallicity"])
        self.ui.refractionLineEdit.setText(material["refraction"])
    
    def fill_material_data(self, material):
        material["color_RGB"]["Red"] = self.ui.lineEdit_Red.text()
        material["color_RGB"]["Green"] = self.ui.lineEdit_Green.text()
        material["color_RGB"]["Blue"] = self.ui.lineEdit_Blue.text()
        material["roughness"] = self.ui.roughnessLineEdit.text()
        material["transparency"] = self.ui.transparencyLineEdit.text()
        material["metallicity"] = self.ui.metallicityLineEdit.text()
        material["refraction"] = self.ui.refractionLineEdit.text()

    @Slot()
    def named_material(self):
        text = self.ui.nameLineEdit.text()
        if self.file and len(text) != 0:
            self.ui.addMaterial.setEnabled(True)
        else:
            self.ui.addMaterial.setEnabled(False)

    @Slot()
    def select_material(self, item):
        material_name = item.text()
        for elem in self.data["features"][0]["Glasses"]:
            if list(elem.keys())[0] == material_name:
                self.ui.deleteMaterial.setEnabled(True)
                self.ui.addMaterial.setEnabled(True)
                self.fill_material_ui(elem)
                break

    @Slot()
    def add_material(self):
        for param in self.ui.material_parametersWidget.findChildren(
            QLineEdit, options=Qt.FindChildOption.FindDirectChildrenOnly
        ):
            if param.text() and not re.match(r"\d+\,?\d*$", param.text()):
                dialog = QMessageBox(icon=QMessageBox.Icon.Critical, parent=self)
                dialog.setWindowTitle("Error")
                dialog.setText('Parameters must be real numbers with ","')
                self.statusBar().showMessage("ERROR")
                dialog.exec()
                return

        material_name = self.ui.nameLineEdit.text()
        find = False
        for elem in self.data["features"][0]["Glasses"]:
            if list(elem.keys())[0] == material_name:
                material = elem[material_name]
                self.fill_material_data(material)
                find = True
                break
        if not find:
            material = copy.deepcopy(info.defaultmaterial)
            self.fill_material_data(material)
            self.data["features"][0]["Glasses"].append({material_name: material})
            self.ui.materialsListWidget.addItem(QListWidgetItem(material_name))
            self.ui.materialsListWidget.setCurrentRow(self.ui.materialsListWidget.count() - 1)
            self.ui.deleteMaterial.setEnabled(True)
        
        self.statusBar().showMessage("Material added")
        self.status_unsaved = "*"
        self.setTitle()

    @Slot()
    def delete_material(self):
        self.ui.addMaterial.setEnabled(False)
        for elem in self.data["features"][0]["Glasses"]:
            if list(elem.keys())[0] == self.ui.materialsListWidget.currentItem().text():
                self.data["features"][0]["Glasses"].remove(elem)
                break
        self.ui.materialsListWidget.takeItem(self.ui.materialsListWidget.currentRow())
        if self.ui.materialsListWidget.count() == 0:
            self.ui.deleteMaterial.setEnabled(False)
            for line_edit in self.ui.materialWidget.findChildren(QLineEdit):
                line_edit.clear()
        else:
            material_name = self.ui.materialsListWidget.currentItem().text()
            for elem in self.data["features"][0]["Glasses"]:
                if list(elem.keys())[0] == material_name:
                    self.ui.deleteMaterial.setEnabled(True)
                    self.ui.addMaterial.setEnabled(True)
                    self.fill_material_ui(elem)
                    break
        self.statusBar().showMessage("Material deleted")
        self.status_unsaved = "*"
        self.setTitle()

    @Slot()
    def add_image(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Open File", "./", "Image (*.jpg)")
        if not filename:
            return
        image = Image.open(filename)
        image = image.resize((256, 256))
        image = image.convert("RGB")
        im_file = BytesIO()
        image.save(im_file, format="JPEG", quality=90)
        encoded_string = base64.b64encode(im_file.getvalue())
        self.ui.tableWidget.setItem(self.items - 2, 1, QTableWidgetItem(str(encoded_string)[2:-1]))
        self.statusBar().showMessage("Image added")

    @Slot()
    def show_image(self):
        try:
            file = BytesIO(base64.b64decode(self.data["features"][0]["properties"]["imageBase64"]))
        except binascii.Error:
            dialog = QMessageBox(icon=QMessageBox.Icon.Critical, parent=self)
            dialog.setWindowTitle("Error")
            dialog.setText("Cannot decode base64 string")
            self.statusBar().showMessage("ERROR")
            dialog.exec()
            return
        try:
            image = Image.open(file)
        except UnidentifiedImageError:
            dialog = QMessageBox(icon=QMessageBox.Icon.Critical, parent=self)
            dialog.setWindowTitle("Error")
            dialog.setText("Cannot identify image")
            self.statusBar().showMessage("ERROR")
            dialog.exec()
            return
        image.show()

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
        if self.data["features"][0]["properties"]["imageBase64"]:
            self.ui.showImage.setEnabled(True)
        else:
            self.ui.showImage.setEnabled(False)
        if self.data["features"][0]["Glasses"]:
            for elem in self.data["features"][0]["Glasses"]:
                self.ui.materialsListWidget.addItem(QListWidgetItem(str(list(elem.keys())[0])))
        self.ui.lineEdit_X.setText(str(self.data["features"][0]["geometry"]["coordinates"][0]))
        self.ui.lineEdit_Y.setText(str(self.data["features"][0]["geometry"]["coordinates"][1]))
        self.ui.addImage.setEnabled(True)
        self.named_material()
        self.named_coordinates()
        self.status_unsaved = ""
        self.setTitle()

    @Slot()
    def newfile(self):
        filename, _ = QFileDialog.getSaveFileName(self, "New File", "./", "JSON (*.geojson *.json)")
        if not filename:
            return
        self.filename = filename
        file = codecs.open(self.filename, "w", "utf-8-sig")
        file.write(json.dumps(info.clear, indent=4, ensure_ascii=False))
        file.close()
        self.openfl()

    @Slot()
    def openfile(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Open File", "./", "JSON (*.geojson *.json)")
        if not filename:
            return
        self.filename = filename
        self.openfl()

    @Slot()
    def saveasfile(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "./", "JSON (*.geojson *.json)")
        if not filename:
            return
        self.filename = filename
        self.savefile()

    @Slot()
    def savefile(self):
        file = codecs.open(self.filename, "w", "utf-8-sig")
        file.write(json.dumps(self.data, indent=4, ensure_ascii=False))
        file.close()
        self.status_unsaved = ""
        self.setTitle()

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
            if key == "imageBase64":
                if item.text():
                    self.ui.showImage.setEnabled(True)
                else:
                    self.ui.showImage.setEnabled(False)
            self.status_unsaved = "*"
            self.setTitle()
            if not self.reundo:
                command = TextChangedCommand(self, item, oldtext)
                self.undoStack.push(command)

    def setTitle(self):
        self.setWindowTitle(f"Editor {self.filename}{self.status_unsaved}")

    def closeEvent(self, event: QCloseEvent) -> None:
        self.ui.tableWidget.reset()
        if self.status_unsaved:
            dialog = QMessageBox(self)
            dialog.addButton(QMessageBox.StandardButton.Yes)
            dialog.addButton(QMessageBox.StandardButton.No)
            dialog.addButton(QMessageBox.StandardButton.Cancel)
            dialog.setWindowTitle("Editor")
            dialog.setText(f'Save changes to "{self.filename}"?')
            dialog.setIcon(QMessageBox.Icon.Warning)
            ret = dialog.exec()
            if ret == QMessageBox.StandardButton.Yes:
                self.savefile()
            elif ret == QMessageBox.StandardButton.No:
                return super().closeEvent(event)
            else:
                return event.ignore()
        return super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow(sys.argv)
    window.show()

    sys.exit(app.exec())
