# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)
from . import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 635)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 818, 524289))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.layoutWidget)
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
        self.whatsapp_page_button = QPushButton(self.icon_text_widget)
        self.whatsapp_page_button.setObjectName(u"whatsapp_page_button")
        self.whatsapp_page_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.whatsapp_page_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Dark icons/facebook.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.whatsapp_page_button.setIcon(icon)
        self.whatsapp_page_button.setIconSize(QSize(30, 23))
        self.whatsapp_page_button.setCheckable(True)
        self.whatsapp_page_button.setChecked(False)
        self.whatsapp_page_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.whatsapp_page_button)

        self.frame_2 = QFrame(self.icon_text_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.manage_page_button = QPushButton(self.frame_2)
        self.manage_page_button.setObjectName(u"manage_page_button")
        self.manage_page_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.manage_page_button.setStyleSheet(u"padding-left : -4px")
        icon1 = QIcon()
        icon1.addFile(u":/Dark icons/cpu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.manage_page_button.setIcon(icon1)
        self.manage_page_button.setIconSize(QSize(25, 25))
        self.manage_page_button.setCheckable(True)
        self.manage_page_button.setChecked(False)
        self.manage_page_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.manage_page_button)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.settings_page_button = QPushButton(self.icon_text_widget)
        self.settings_page_button.setObjectName(u"settings_page_button")
        self.settings_page_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.settings_page_button.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/Dark icons/grid.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_page_button.setIcon(icon2)
        self.settings_page_button.setIconSize(QSize(73, 25))
        self.settings_page_button.setCheckable(True)
        self.settings_page_button.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.settings_page_button)

        self.timers_page_button = QPushButton(self.icon_text_widget)
        self.timers_page_button.setObjectName(u"timers_page_button")
        self.timers_page_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.timers_page_button.setStyleSheet(u"")
        self.timers_page_button.setIcon(icon2)
        self.timers_page_button.setIconSize(QSize(73, 25))
        self.timers_page_button.setCheckable(True)
        self.timers_page_button.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.timers_page_button)

        self.message_page_button = QPushButton(self.icon_text_widget)
        self.message_page_button.setObjectName(u"message_page_button")
        self.message_page_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.message_page_button.setStyleSheet(u"")
        self.message_page_button.setIcon(icon2)
        self.message_page_button.setIconSize(QSize(73, 25))
        self.message_page_button.setCheckable(True)
        self.message_page_button.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.message_page_button)

        self.frame = QFrame(self.icon_text_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_4.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 16777019, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.icon_text_widget, 1, 1, 1, 1)

        self.main_window_widget = QWidget(self.layoutWidget)
        self.main_window_widget.setObjectName(u"main_window_widget")
        self.main_window_widget.setMinimumSize(QSize(630, 550))
        self.main_window_widget.setStyleSheet(u"background-color : rgb(78, 255, 158)")
        self.layoutWidget1 = QWidget(self.main_window_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 601, 511))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.layoutWidget1)
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
        self.save_cookies = QPushButton(self.page_2)
        self.save_cookies.setObjectName(u"save_cookies")
        self.save_cookies.setGeometry(QRect(450, 110, 101, 41))
        self.save_cookies.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.load_cookies = QPushButton(self.page_2)
        self.load_cookies.setObjectName(u"load_cookies")
        self.load_cookies.setGeometry(QRect(450, 40, 101, 41))
        self.load_cookies.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.attachment_button_val = QPlainTextEdit(self.page_2)
        self.attachment_button_val.setObjectName(u"attachment_button_val")
        self.attachment_button_val.setGeometry(QRect(10, 210, 391, 31))
        self.attachment_button_val.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.send_message_button_text = QPlainTextEdit(self.page_2)
        self.send_message_button_text.setObjectName(u"send_message_button_text")
        self.send_message_button_text.setGeometry(QRect(10, 300, 391, 31))
        self.send_message_button_text.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.send_button_value = QPlainTextEdit(self.page_2)
        self.send_button_value.setObjectName(u"send_button_value")
        self.send_button_value.setGeometry(QRect(10, 370, 391, 31))
        self.send_button_value.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.image_attachment_accept_value = QPlainTextEdit(self.page_2)
        self.image_attachment_accept_value.setObjectName(u"image_attachment_accept_value")
        self.image_attachment_accept_value.setGeometry(QRect(10, 440, 181, 31))
        self.image_attachment_accept_value.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 250, 161, 41))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 330, 161, 41))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 160, 161, 41))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 400, 151, 41))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.invalid_modal_okay_button_class = QPlainTextEdit(self.page_2)
        self.invalid_modal_okay_button_class.setObjectName(u"invalid_modal_okay_button_class")
        self.invalid_modal_okay_button_class.setGeometry(QRect(10, 130, 391, 31))
        self.invalid_modal_okay_button_class.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 80, 251, 41))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.invalid_modal_text = QPlainTextEdit(self.page_2)
        self.invalid_modal_text.setObjectName(u"invalid_modal_text")
        self.invalid_modal_text.setGeometry(QRect(10, 40, 391, 31))
        self.invalid_modal_text.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 0, 251, 41))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.save_settings_button = QPushButton(self.page_2)
        self.save_settings_button.setObjectName(u"save_settings_button")
        self.save_settings_button.setGeometry(QRect(450, 420, 101, 41))
        self.save_settings_button.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.file_attachment_accept_value = QPlainTextEdit(self.page_2)
        self.file_attachment_accept_value.setObjectName(u"file_attachment_accept_value")
        self.file_attachment_accept_value.setGeometry(QRect(200, 440, 201, 31))
        self.file_attachment_accept_value.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(200, 400, 151, 41))
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"font-weight : bold;\n"
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
        self.load_image_btn = QPushButton(self.page_3)
        self.load_image_btn.setObjectName(u"load_image_btn")
        self.load_image_btn.setGeometry(QRect(430, 200, 111, 31))
        self.load_image_btn.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.load_image_btn.setCheckable(True)
        self.load_image_btn.setAutoExclusive(True)
        self.load_csv_btn = QPushButton(self.page_3)
        self.load_csv_btn.setObjectName(u"load_csv_btn")
        self.load_csv_btn.setGeometry(QRect(430, 130, 111, 31))
        self.load_csv_btn.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.load_csv_btn.setCheckable(True)
        self.load_csv_btn.setAutoExclusive(True)
        self.excel_text_edit = QPlainTextEdit(self.page_3)
        self.excel_text_edit.setObjectName(u"excel_text_edit")
        self.excel_text_edit.setGeometry(QRect(10, 130, 391, 31))
        self.excel_text_edit.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.image_text_edit = QPlainTextEdit(self.page_3)
        self.image_text_edit.setObjectName(u"image_text_edit")
        self.image_text_edit.setGeometry(QRect(10, 200, 381, 31))
        self.image_text_edit.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.create_sample_csv_button = QPushButton(self.page_3)
        self.create_sample_csv_button.setObjectName(u"create_sample_csv_button")
        self.create_sample_csv_button.setGeometry(QRect(10, 70, 131, 31))
        self.create_sample_csv_button.setStyleSheet(u"QPushButton{\n"
"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"}\n"
"")
        self.create_sample_csv_button.setCheckable(True)
        self.create_sample_csv_button.setAutoExclusive(True)
        self.not_sent_numbers_button = QPushButton(self.page_3)
        self.not_sent_numbers_button.setObjectName(u"not_sent_numbers_button")
        self.not_sent_numbers_button.setGeometry(QRect(130, 340, 131, 31))
        self.not_sent_numbers_button.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.not_sent_numbers_button.setCheckable(True)
        self.not_sent_numbers_button.setAutoExclusive(True)
        self.sent_numbers_button = QPushButton(self.page_3)
        self.sent_numbers_button.setObjectName(u"sent_numbers_button")
        self.sent_numbers_button.setGeometry(QRect(10, 340, 101, 31))
        self.sent_numbers_button.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.sent_numbers_button.setCheckable(True)
        self.sent_numbers_button.setAutoExclusive(True)
        self.invalid_numbers_button = QPushButton(self.page_3)
        self.invalid_numbers_button.setObjectName(u"invalid_numbers_button")
        self.invalid_numbers_button.setGeometry(QRect(280, 340, 121, 31))
        self.invalid_numbers_button.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.invalid_numbers_button.setCheckable(True)
        self.invalid_numbers_button.setAutoExclusive(True)
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 260, 421, 51))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.wait_time_spin_box = QSpinBox(self.page_4)
        self.wait_time_spin_box.setObjectName(u"wait_time_spin_box")
        self.wait_time_spin_box.setGeometry(QRect(20, 150, 91, 31))
        self.wait_time_spin_box.setBaseSize(QSize(6, 4))
        self.wait_time_spin_box.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.label_2 = QLabel(self.page_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 161, 61))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.label_16 = QLabel(self.page_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 100, 81, 41))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.upload_time_spin_box = QSpinBox(self.page_4)
        self.upload_time_spin_box.setObjectName(u"upload_time_spin_box")
        self.upload_time_spin_box.setGeometry(QRect(150, 150, 91, 31))
        self.upload_time_spin_box.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.label_17 = QLabel(self.page_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(150, 100, 101, 41))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.sleep_time_spin_box = QSpinBox(self.page_4)
        self.sleep_time_spin_box.setObjectName(u"sleep_time_spin_box")
        self.sleep_time_spin_box.setGeometry(QRect(270, 150, 91, 31))
        self.sleep_time_spin_box.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.label_19 = QLabel(self.page_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(270, 100, 101, 41))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 421, 81))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font-weight : bold;\n"
"color : black;")
        self.custom_message = QPlainTextEdit(self.page_5)
        self.custom_message.setObjectName(u"custom_message")
        self.custom_message.setGeometry(QRect(20, 110, 521, 311))
        self.custom_message.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;\n"
"padding-top : 3px;\n"
"padding-left : 5px;")
        self.save_custom_message_button = QPushButton(self.page_5)
        self.save_custom_message_button.setObjectName(u"save_custom_message_button")
        self.save_custom_message_button.setGeometry(QRect(440, 430, 101, 41))
        self.save_custom_message_button.setStyleSheet(u"background-color : black;\n"
"color : white;\n"
"border-radius : 10px;")
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.main_window_widget, 1, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 2)

        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")

        self.gridLayout_2.addWidget(self.header_widget, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.whatsapp_page_button.setText(QCoreApplication.translate("MainWindow", u"       Whatsapp ", None))
        self.manage_page_button.setText(QCoreApplication.translate("MainWindow", u"       Manage   ", None))
        self.settings_page_button.setText(QCoreApplication.translate("MainWindow", u"         Settings", None))
        self.timers_page_button.setText(QCoreApplication.translate("MainWindow", u"         Timers", None))
        self.message_page_button.setText(QCoreApplication.translate("MainWindow", u"      Messages", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.open_whatsapp_button.setText(QCoreApplication.translate("MainWindow", u"Open WhatsApp", None))
        self.select_message_type_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))

#if QT_CONFIG(tooltip)
        self.select_message_type_combo_box.setToolTip(QCoreApplication.translate("MainWindow", u"Select Option", None))
#endif // QT_CONFIG(tooltip)
        self.send_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.save_cookies.setText(QCoreApplication.translate("MainWindow", u"Save Cookies", None))
        self.load_cookies.setText(QCoreApplication.translate("MainWindow", u"Load Cookies", None))
        self.attachment_button_val.setPlainText("")
        self.send_message_button_text.setPlainText("")
        self.send_button_value.setPlainText("")
        self.image_attachment_accept_value.setPlainText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"send_message_button_text", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"send_button_value", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"attachment_button_val", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"image_attachment", None))
        self.invalid_modal_okay_button_class.setPlainText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"invalid_modal_okay_button_class", None))
#if QT_CONFIG(accessibility)
        self.invalid_modal_text.setAccessibleName(QCoreApplication.translate("MainWindow", u"invalid_modal_text", None))
#endif // QT_CONFIG(accessibility)
        self.invalid_modal_text.setPlainText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"invalid_modal_text", None))
        self.save_settings_button.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.file_attachment_accept_value.setPlainText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"File_attachment", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Mange Files", None))
        self.load_image_btn.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.load_csv_btn.setText(QCoreApplication.translate("MainWindow", u"Load Excel", None))
        self.excel_text_edit.setPlainText("")
        self.create_sample_csv_button.setText(QCoreApplication.translate("MainWindow", u"Create Sample CSV", None))
        self.not_sent_numbers_button.setText(QCoreApplication.translate("MainWindow", u"Not Sent Numbers", None))
        self.sent_numbers_button.setText(QCoreApplication.translate("MainWindow", u"Sent Numbers", None))
        self.invalid_numbers_button.setText(QCoreApplication.translate("MainWindow", u"Invalid Numbers", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Export Numbers", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Timers", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"wait time", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"upload time", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"sleep time", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Load Message with commas", None))
        self.custom_message.setPlainText("")
        self.save_custom_message_button.setText(QCoreApplication.translate("MainWindow", u"Save Message", None))
    # retranslateUi

