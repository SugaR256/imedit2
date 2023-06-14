# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 715)
        self.verticalLayoutWidget = QWidget(MainWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 49, 251, 531))
        self.tools = QVBoxLayout(self.verticalLayoutWidget)
        self.tools.setObjectName(u"tools")
        self.tools.setContentsMargins(0, 0, 0, 0)
        self.openButton = QPushButton(self.verticalLayoutWidget)
        self.openButton.setObjectName(u"openButton")

        self.tools.addWidget(self.openButton)

        self.saveButton = QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName(u"saveButton")

        self.tools.addWidget(self.saveButton)

        self.saveAsButton = QPushButton(self.verticalLayoutWidget)
        self.saveAsButton.setObjectName(u"saveAsButton")

        self.tools.addWidget(self.saveAsButton)

        self.brightnessButton = QPushButton(self.verticalLayoutWidget)
        self.brightnessButton.setObjectName(u"brightnessButton")

        self.tools.addWidget(self.brightnessButton)

        self.contrastButton = QPushButton(self.verticalLayoutWidget)
        self.contrastButton.setObjectName(u"contrastButton")

        self.tools.addWidget(self.contrastButton)

        self.cropButton = QPushButton(self.verticalLayoutWidget)
        self.cropButton.setObjectName(u"cropButton")

        self.tools.addWidget(self.cropButton)

        self.saturationButton = QPushButton(self.verticalLayoutWidget)
        self.saturationButton.setObjectName(u"saturationButton")

        self.tools.addWidget(self.saturationButton)

        self.sharpnessButton = QPushButton(self.verticalLayoutWidget)
        self.sharpnessButton.setObjectName(u"sharpnessButton")

        self.tools.addWidget(self.sharpnessButton)

        self.blurButton = QPushButton(self.verticalLayoutWidget)
        self.blurButton.setObjectName(u"blurButton")

        self.tools.addWidget(self.blurButton)

        self.findEdgesButton = QPushButton(self.verticalLayoutWidget)
        self.findEdgesButton.setObjectName(u"findEdgesButton")

        self.tools.addWidget(self.findEdgesButton)

        self.enhanceEdgesButton = QPushButton(self.verticalLayoutWidget)
        self.enhanceEdgesButton.setObjectName(u"enhanceEdgesButton")

        self.tools.addWidget(self.enhanceEdgesButton)

        self.identifyButton = QPushButton(self.verticalLayoutWidget)
        self.identifyButton.setObjectName(u"identifyButton")

        self.tools.addWidget(self.identifyButton)

        self.horizontalLayoutWidget = QWidget(MainWindow)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(279, 49, 1201, 531))
        self.images = QHBoxLayout(self.horizontalLayoutWidget)
        self.images.setObjectName(u"images")
        self.images.setContentsMargins(0, 0, 0, 0)
        self.imageField = QLabel(self.horizontalLayoutWidget)
        self.imageField.setObjectName(u"imageField")
        self.imageField.setScaledContents(False)
        self.imageField.setAlignment(Qt.AlignCenter)

        self.images.addWidget(self.imageField)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.images.addItem(self.horizontalSpacer)

        self.originalImageField = QLabel(self.horizontalLayoutWidget)
        self.originalImageField.setObjectName(u"originalImageField")
        self.originalImageField.setScaledContents(False)
        self.originalImageField.setAlignment(Qt.AlignCenter)

        self.images.addWidget(self.originalImageField)

        self.histogramLabel = QLabel(MainWindow)
        self.histogramLabel.setObjectName(u"histogramLabel")
        self.histogramLabel.setGeometry(QRect(690, 590, 331, 121))
        self.histogramLabel.setFrameShape(QFrame.Box)
        self.histogramLabel.setScaledContents(True)
        self.histogramLabel.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(MainWindow)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 590, 671, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.creationDate = QDateTimeEdit(self.gridLayoutWidget)
        self.creationDate.setObjectName(u"creationDate")
        self.creationDate.setEnabled(True)
        self.creationDate.setFrame(True)
        self.creationDate.setReadOnly(False)
        self.creationDate.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.creationDate)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.heightLabel = QLabel(self.gridLayoutWidget)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.heightLabel)


        self.horizontalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.modificationDate = QDateTimeEdit(self.gridLayoutWidget)
        self.modificationDate.setObjectName(u"modificationDate")
        self.modificationDate.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.modificationDate)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.depthLabel = QLabel(self.gridLayoutWidget)
        self.depthLabel.setObjectName(u"depthLabel")
        self.depthLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.depthLabel)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.sizeLabel = QLabel(self.gridLayoutWidget)
        self.sizeLabel.setObjectName(u"sizeLabel")
        self.sizeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.sizeLabel)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.widthLabel = QLabel(self.gridLayoutWidget)
        self.widthLabel.setObjectName(u"widthLabel")
        self.widthLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.widthLabel)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_7)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.undoButton = QPushButton(MainWindow)
        self.undoButton.setObjectName(u"undoButton")
        self.undoButton.setEnabled(False)
        self.undoButton.setGeometry(QRect(400, 10, 93, 29))
        self.undoButton.setCheckable(False)
        self.redoButton = QPushButton(MainWindow)
        self.redoButton.setObjectName(u"redoButton")
        self.redoButton.setEnabled(False)
        self.redoButton.setGeometry(QRect(500, 10, 93, 29))
        self.label_4 = QLabel(MainWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 391, 41))
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.turnLeftButton = QPushButton(MainWindow)
        self.turnLeftButton.setObjectName(u"turnLeftButton")
        self.turnLeftButton.setGeometry(QRect(1030, 590, 121, 51))
        self.turnRightButton = QPushButton(MainWindow)
        self.turnRightButton.setObjectName(u"turnRightButton")
        self.turnRightButton.setGeometry(QRect(1030, 660, 121, 51))
        self.itemsList = QTableWidget(MainWindow)
        if (self.itemsList.columnCount() < 2):
            self.itemsList.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.itemsList.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.itemsList.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.itemsList.setObjectName(u"itemsList")
        self.itemsList.setGeometry(QRect(1160, 590, 321, 121))
        self.itemsList.setRowCount(0)
        self.itemsList.setColumnCount(2)
        self.itemsList.horizontalHeader().setMinimumSectionSize(42)
        self.itemsList.verticalHeader().setMinimumSectionSize(29)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ImEdit by Jakub Kr\u0105piec", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"Otw\u00f3rz", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.saveAsButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz jako...", None))
        self.brightnessButton.setText(QCoreApplication.translate("MainWindow", u"Jasno\u015b\u0107", None))
        self.contrastButton.setText(QCoreApplication.translate("MainWindow", u"Kontrast", None))
        self.cropButton.setText(QCoreApplication.translate("MainWindow", u"Przytnij", None))
        self.saturationButton.setText(QCoreApplication.translate("MainWindow", u"Nasycenie", None))
        self.sharpnessButton.setText(QCoreApplication.translate("MainWindow", u"Ostro\u015b\u0107", None))
        self.blurButton.setText(QCoreApplication.translate("MainWindow", u"Rozmycie Gaussa", None))
        self.findEdgesButton.setText(QCoreApplication.translate("MainWindow", u"Znajd\u017a kraw\u0119dzie", None))
        self.enhanceEdgesButton.setText(QCoreApplication.translate("MainWindow", u"Popraw kraw\u0119dzie", None))
        self.identifyButton.setText(QCoreApplication.translate("MainWindow", u"Zidentyfikuj obiekty", None))
        self.imageField.setText(QCoreApplication.translate("MainWindow", u"Otw\u00f3rz zdj\u0119cie, aby rozpocz\u0105\u0107 edytowanie", None))
        self.originalImageField.setText(QCoreApplication.translate("MainWindow", u"Tutaj b\u0119dzie widoczny oryginalny obraz", None))
        self.histogramLabel.setText(QCoreApplication.translate("MainWindow", u"Histogram", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Data utworzenia", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Wysoko\u015b\u0107", None))
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"0 px", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data ostatniej modyfikacji", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"G\u0142\u0119bia kolor\u00f3w", None))
        self.depthLabel.setText(QCoreApplication.translate("MainWindow", u"0 b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rozmiar", None))
        self.sizeLabel.setText(QCoreApplication.translate("MainWindow", u"0 B", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Szeroko\u015b\u0107", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"0 px", None))
        self.undoButton.setText(QCoreApplication.translate("MainWindow", u"Cofnij", None))
        self.redoButton.setText(QCoreApplication.translate("MainWindow", u"Pon\u00f3w", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ImEdit by Jakub Kr\u0105piec", None))
        self.turnLeftButton.setText(QCoreApplication.translate("MainWindow", u"Obr\u00f3\u0107 w lewo", None))
        self.turnRightButton.setText(QCoreApplication.translate("MainWindow", u"Obr\u00f3\u0107 w prawo", None))
        ___qtablewidgetitem = self.itemsList.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nazwa obiektu", None));
        ___qtablewidgetitem1 = self.itemsList.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pewno\u015b\u0107", None));
    # retranslateUi

