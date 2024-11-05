# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(811, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 818, 524289))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.widget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(129, 0))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color : black;\n"
"	color : white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	height : 25px;\n"
"    border : none;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_13 = QPushButton(self.icon_text_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_13.setStyleSheet(u"QPushButton:checked{\n"
"	background-color : white;\n"
"	border-radius : 3px;\n"
"	color : black;\n"
"padding : 3px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Dark icons/facebook.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/facebook.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon.addFile(u":/Dark icons/facebook.svg", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon.addFile(u":/icons/facebook.svg", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.pushButton_13.setIcon(icon)
        self.pushButton_13.setIconSize(QSize(30, 23))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_13)

        self.frame_2 = QFrame(self.icon_text_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_4.setStyleSheet(u"QPushButton:checked{\n"
"	background-color : white;\n"
"	border-radius : 3px;\n"
"	color : black;\n"
"padding : 3px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Dark icons/cpu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/cpu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(25, 25))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.pushButton_12 = QPushButton(self.icon_text_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_12.setStyleSheet(u"QPushButton:checked{\n"
"	background-color : white;\n"
"	border-radius : 3px;\n"
"	color : black;\n"
"padding : 3px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Dark icons/grid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/grid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QSize(73, 25))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_12)

        self.frame = QFrame(self.icon_text_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_4.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 16777019, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.icon_text_widget, 1, 1, 1, 1)

        self.main_window_widget = QWidget(self.widget)
        self.main_window_widget.setObjectName(u"main_window_widget")
        self.main_window_widget.setMinimumSize(QSize(630, 550))
        self.main_window_widget.setStyleSheet(u"background-color : rgb(78, 255, 158)")
        self.layoutWidget = QWidget(self.main_window_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 601, 511))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 161, 61))
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.open_whatsapp_button = QPushButton(self.page)
        self.open_whatsapp_button.setObjectName(u"open_whatsapp_button")
        self.open_whatsapp_button.setGeometry(QRect(30, 120, 111, 41))
        self.open_whatsapp_button.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.select_message_type_combo_box = QComboBox(self.page)
        self.select_message_type_combo_box.addItem("")
        self.select_message_type_combo_box.setObjectName(u"select_message_type_combo_box")
        self.select_message_type_combo_box.setGeometry(QRect(30, 190, 271, 41))
        self.select_message_type_combo_box.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-left :20px")
        self.send_button = QPushButton(self.page)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QRect(340, 190, 101, 41))
        self.send_button.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 161, 61))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 421, 51))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.load_image = QPushButton(self.page_3)
        self.load_image.setObjectName(u"load_image")
        self.load_image.setGeometry(QRect(430, 200, 101, 31))
        self.load_image.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.openWhatsapp_button_2 = QPushButton(self.page_3)
        self.openWhatsapp_button_2.setObjectName(u"openWhatsapp_button_2")
        self.openWhatsapp_button_2.setGeometry(QRect(430, 130, 111, 31))
        self.openWhatsapp_button_2.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.excel_text_edit = QPlainTextEdit(self.page_3)
        self.excel_text_edit.setObjectName(u"excel_text_edit")
        self.excel_text_edit.setGeometry(QRect(10, 130, 391, 31))
        self.excel_text_edit.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.excel_text_edit_2 = QPlainTextEdit(self.page_3)
        self.excel_text_edit_2.setObjectName(u"excel_text_edit_2")
        self.excel_text_edit_2.setGeometry(QRect(10, 200, 381, 31))
        self.excel_text_edit_2.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.main_window_widget, 1, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 2)

        self.header_widget = QWidget(self.widget)
        self.header_widget.setObjectName(u"header_widget")

        self.gridLayout_2.addWidget(self.header_widget, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"       Whatsapp ", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"       Manage   ", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"         Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.open_whatsapp_button.setText(QCoreApplication.translate("MainWindow", u"Open WhatsApp", None))
        self.select_message_type_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))

#if QT_CONFIG(tooltip)
        self.select_message_type_combo_box.setToolTip(QCoreApplication.translate("MainWindow", u"Select Option", None))
#endif // QT_CONFIG(tooltip)
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mange Files", None))
        self.load_image.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.openWhatsapp_button_2.setText(QCoreApplication.translate("MainWindow", u"Load Excel", None))
    # retranslateUi

