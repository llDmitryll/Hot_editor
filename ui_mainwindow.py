# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFormLayout, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class QLineEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)
    def enterEvent(self, event):
        return

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 744)
        MainWindow.setMouseTracking(False)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionsave_as = QAction(MainWindow)
        self.actionsave_as.setObjectName(u"actionsave_as")
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(410, 0))
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tableWidget.setFrameShape(QFrame.Shape.Box)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tableWidget)

        self.informationWidget = QWidget(self.centralwidget)
        self.informationWidget.setObjectName(u"informationWidget")
        self.informationWidget.setMinimumSize(QSize(300, 0))
        self.informationWidget.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.informationWidget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.materialsListWidget = QListWidget(self.informationWidget)
        self.materialsListWidget.setObjectName(u"materialsListWidget")
        self.materialsListWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHeightForWidth(self.materialsListWidget.sizePolicy().hasHeightForWidth())
        self.materialsListWidget.setSizePolicy(sizePolicy)
        self.materialsListWidget.setMinimumSize(QSize(266, 100))
        self.materialsListWidget.setMaximumSize(QSize(266, 100))
        self.materialsListWidget.setFrameShape(QFrame.Shape.Box)
        self.materialsListWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.materialsListWidget.setLineWidth(1)
        self.materialsListWidget.setMidLineWidth(0)

        self.verticalLayout_2.addWidget(self.materialsListWidget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.materialWidget = QWidget(self.informationWidget)
        self.materialWidget.setObjectName(u"materialWidget")
        sizePolicy.setHeightForWidth(self.materialWidget.sizePolicy().hasHeightForWidth())
        self.materialWidget.setSizePolicy(sizePolicy)
        self.materialWidget.setMinimumSize(QSize(0, 270))
        self.materialWidget.setMaximumSize(QSize(1000000, 250))
        self.materialWidget.setBaseSize(QSize(0, 0))
        self.formLayout = QFormLayout(self.materialWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.nameLabel = QLabel(self.materialWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.materialWidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setMinimumSize(QSize(240, 20))
        self.nameLineEdit.setMaximumSize(QSize(240, 20))
        self.nameLineEdit.setMouseTracking(False)
        self.nameLineEdit.setFrame(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.colorLabel = QLabel(self.materialWidget)
        self.colorLabel.setObjectName(u"colorLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.colorLabel)

        self.colorWidget = QWidget(self.materialWidget)
        self.colorWidget.setObjectName(u"colorWidget")
        self.colorWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.colorWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 0, 12, 0)
        self.label_Red = QLabel(self.colorWidget)
        self.label_Red.setObjectName(u"label_Red")

        self.horizontalLayout_2.addWidget(self.label_Red)

        self.lineEdit_Red = QLineEdit(self.colorWidget)
        self.lineEdit_Red.setObjectName(u"lineEdit_Red")
        self.lineEdit_Red.setMinimumSize(QSize(63, 20))
        self.lineEdit_Red.setMaximumSize(QSize(63, 20))
        self.lineEdit_Red.setMouseTracking(False)
        self.lineEdit_Red.setFrame(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_Red)

        self.label_Green = QLabel(self.colorWidget)
        self.label_Green.setObjectName(u"label_Green")

        self.horizontalLayout_2.addWidget(self.label_Green)

        self.lineEdit_Green = QLineEdit(self.colorWidget)
        self.lineEdit_Green.setObjectName(u"lineEdit_Green")
        self.lineEdit_Green.setMinimumSize(QSize(63, 20))
        self.lineEdit_Green.setMaximumSize(QSize(63, 20))
        self.lineEdit_Green.setMouseTracking(False)
        self.lineEdit_Green.setFrame(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_Green)

        self.label_Blue = QLabel(self.colorWidget)
        self.label_Blue.setObjectName(u"label_Blue")

        self.horizontalLayout_2.addWidget(self.label_Blue)

        self.lineEdit_Blue = QLineEdit(self.colorWidget)
        self.lineEdit_Blue.setObjectName(u"lineEdit_Blue")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_Blue.sizePolicy().hasHeightForWidth())
        self.lineEdit_Blue.setSizePolicy(sizePolicy1)
        self.lineEdit_Blue.setMinimumSize(QSize(63, 20))
        self.lineEdit_Blue.setMaximumSize(QSize(63, 20))
        self.lineEdit_Blue.setMouseTracking(False)
        self.lineEdit_Blue.setFrame(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_Blue)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.colorWidget)

        self.material_parametersWidget = QWidget(self.materialWidget)
        self.material_parametersWidget.setObjectName(u"material_parametersWidget")
        self.formLayout_3 = QFormLayout(self.material_parametersWidget)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.transparencyLabel = QLabel(self.material_parametersWidget)
        self.transparencyLabel.setObjectName(u"transparencyLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.transparencyLabel)

        self.transparencyLineEdit = QLineEdit(self.material_parametersWidget)
        self.transparencyLineEdit.setObjectName(u"transparencyLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.transparencyLineEdit.sizePolicy().hasHeightForWidth())
        self.transparencyLineEdit.setSizePolicy(sizePolicy2)
        self.transparencyLineEdit.setFixedHeight(22)
        self.transparencyLineEdit.setAutoFillBackground(False)
        self.transparencyLineEdit.setFrame(True)
        self.transparencyLineEdit.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.transparencyLineEdit)

        self.refractionLabel = QLabel(self.material_parametersWidget)
        self.refractionLabel.setObjectName(u"refractionLabel")
        self.refractionLabel.setMinimumSize(QSize(0, 0))

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.refractionLabel)

        self.refractionLineEdit = QLineEdit(self.material_parametersWidget)
        self.refractionLineEdit.setObjectName(u"refractionLineEdit")
        self.refractionLineEdit.setFixedHeight(22)
        self.refractionLineEdit.setFrame(True)
        self.refractionLineEdit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.refractionLineEdit)

        self.roughnessLabel = QLabel(self.material_parametersWidget)
        self.roughnessLabel.setObjectName(u"roughnessLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.roughnessLabel)

        self.roughnessLineEdit = QLineEdit(self.material_parametersWidget)
        self.roughnessLineEdit.setObjectName(u"roughnessLineEdit")
        self.roughnessLineEdit.setFixedHeight(22)
        self.roughnessLineEdit.setFrame(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.roughnessLineEdit)

        self.metallicityLabel = QLabel(self.material_parametersWidget)
        self.metallicityLabel.setObjectName(u"metallicityLabel")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.metallicityLabel)

        self.metallicityLineEdit = QLineEdit(self.material_parametersWidget)
        self.metallicityLineEdit.setObjectName(u"metallicityLineEdit")
        self.metallicityLineEdit.setFixedHeight(22)
        self.metallicityLineEdit.setFrame(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.metallicityLineEdit)


        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.material_parametersWidget)

        self.addMaterial = QPushButton(self.materialWidget)
        self.addMaterial.setObjectName(u"addMaterial")
        self.addMaterial.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.addMaterial)

        self.deleteMaterial = QPushButton(self.materialWidget)
        self.deleteMaterial.setObjectName(u"deleteMaterial")
        self.deleteMaterial.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.deleteMaterial)

        self.selectColor = QPushButton(self.materialWidget)
        self.selectColor.setObjectName(u"selectColor")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.selectColor.sizePolicy().hasHeightForWidth())
        self.selectColor.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.selectColor)


        self.verticalLayout_2.addWidget(self.materialWidget, 0, Qt.AlignmentFlag.AlignTop)

        self.addImage = QPushButton(self.informationWidget)
        self.addImage.setObjectName(u"addImage")
        self.addImage.setEnabled(False)

        self.verticalLayout_2.addWidget(self.addImage)

        self.showImage = QPushButton(self.informationWidget)
        self.showImage.setObjectName(u"showImage")
        self.showImage.setEnabled(False)

        self.verticalLayout_2.addWidget(self.showImage)

        self.coordinatesWidget = QWidget(self.informationWidget)
        self.coordinatesWidget.setObjectName(u"coordinatesWidget")
        self.formLayout_2 = QFormLayout(self.coordinatesWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.coordinatesLabel = QLabel(self.coordinatesWidget)
        self.coordinatesLabel.setObjectName(u"coordinatesLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.coordinatesLabel)

        self.coordinates_inputWidget = QWidget(self.coordinatesWidget)
        self.coordinates_inputWidget.setObjectName(u"coordinates_inputWidget")
        sizePolicy.setHeightForWidth(self.coordinates_inputWidget.sizePolicy().hasHeightForWidth())
        self.coordinates_inputWidget.setSizePolicy(sizePolicy)
        self.coordinates_inputWidget.setMouseTracking(False)
        self.verticalLayout = QVBoxLayout(self.coordinates_inputWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_X = QLabel(self.coordinates_inputWidget)
        self.label_X.setObjectName(u"label_X")

        self.verticalLayout.addWidget(self.label_X)

        self.lineEdit_X = QLineEdit(self.coordinates_inputWidget)
        self.lineEdit_X.setObjectName(u"lineEdit_X")
        self.lineEdit_X.setMinimumSize(QSize(0, 20))
        self.lineEdit_X.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_X.setSizeIncrement(QSize(0, 0))
        self.lineEdit_X.setFrame(True)

        self.verticalLayout.addWidget(self.lineEdit_X)

        self.label_Y = QLabel(self.coordinates_inputWidget)
        self.label_Y.setObjectName(u"label_Y")

        self.verticalLayout.addWidget(self.label_Y)

        self.lineEdit_Y = QLineEdit(self.coordinates_inputWidget)
        self.lineEdit_Y.setObjectName(u"lineEdit_Y")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_Y.sizePolicy().hasHeightForWidth())
        self.lineEdit_Y.setSizePolicy(sizePolicy4)
        self.lineEdit_Y.setMinimumSize(QSize(0, 20))
        self.lineEdit_Y.setMaximumSize(QSize(16777215, 20))
        self.lineEdit_Y.setSizeIncrement(QSize(0, 0))
        self.lineEdit_Y.setBaseSize(QSize(0, 0))
        self.lineEdit_Y.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.lineEdit_Y.setFrame(True)

        self.verticalLayout.addWidget(self.lineEdit_Y)


        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.coordinates_inputWidget)

        self.addCoord = QPushButton(self.coordinatesWidget)
        self.addCoord.setObjectName(u"addCoord")
        self.addCoord.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.SpanningRole, self.addCoord)


        self.verticalLayout_2.addWidget(self.coordinatesWidget)


        self.horizontalLayout.addWidget(self.informationWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 932, 22))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionsave_as)
        self.menufile.addAction(self.actionnew)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionsave_as.setText(QCoreApplication.translate("MainWindow", u"save as", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"new", None))
#if QT_CONFIG(shortcut)
        self.actionnew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Key", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.colorLabel.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_Red.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_Green.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_Blue.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.transparencyLabel.setText(QCoreApplication.translate("MainWindow", u"transparency", None))
        self.refractionLabel.setText(QCoreApplication.translate("MainWindow", u"refraction", None))
        self.roughnessLabel.setText(QCoreApplication.translate("MainWindow", u"roughness", None))
        self.metallicityLabel.setText(QCoreApplication.translate("MainWindow", u"metallicity", None))
        self.addMaterial.setText(QCoreApplication.translate("MainWindow", u"Add Material", None))
        self.deleteMaterial.setText(QCoreApplication.translate("MainWindow", u"Delete Material", None))
        self.selectColor.setText(QCoreApplication.translate("MainWindow", u"Select Color", None))
        self.addImage.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.showImage.setText(QCoreApplication.translate("MainWindow", u"Show Image", None))
        self.coordinatesLabel.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.label_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.addCoord.setText(QCoreApplication.translate("MainWindow", u"Add coodrinates", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
    # retranslateUi

