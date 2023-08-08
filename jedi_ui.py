# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'graphics.ui'
##
# Created by: Qt User Interface Compiler version 6.5.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
                               QSpinBox, QStatusBar, QTextBrowser, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(775, 786)
        palette = QPalette()
        brush = QBrush(QColor(205, 215, 255, 216))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(138, 173, 191, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        brush2 = QBrush(QColor(210, 232, 255, 216))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush3 = QBrush(QColor(197, 221, 255, 216))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush4 = QBrush(QColor(178, 214, 255, 216))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush4)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font = QFont()
        font.setFamilies([u"Herculanum"])
        font.setPointSize(14)
        font.setItalic(True)
        self.pushButton_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalSpacer = QSpacerItem(
            120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setFamilies([u"Herculanum"])
        font1.setPointSize(18)
        font1.setItalic(True)
        self.label_5.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.next_host = QComboBox(self.centralwidget)
        self.next_host.setObjectName(u"next_host")
        self.next_host.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_3.addWidget(self.next_host)

        self.horizontalSpacer_2 = QSpacerItem(
            10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setFont(font1)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setMargin(7)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.next_port = QSpinBox(self.centralwidget)
        self.next_port.setObjectName(u"next_port")
        self.next_port.setMinimumSize(QSize(80, 0))
        self.next_port.setMinimum(1)
        self.next_port.setMaximum(9999)
        self.next_port.setValue(80)

        self.horizontalLayout_3.addWidget(self.next_port)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 1, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Herculanum"])
        font2.setPointSize(48)
        font2.setItalic(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_10)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamilies([u"Herculanum"])
        font3.setPointSize(24)
        font3.setItalic(True)
        self.label_3.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_3)

        self.remote_host = QComboBox(self.centralwidget)
        self.remote_host.setObjectName(u"remote_host")

        self.verticalLayout_5.addWidget(self.remote_host)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_5)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_2)

        self.remote_port = QSpinBox(self.centralwidget)
        self.remote_port.setObjectName(u"remote_port")
        self.remote_port.setMinimum(1)
        self.remote_port.setMaximum(9999)
        self.remote_port.setValue(22)

        self.verticalLayout_5.addWidget(self.remote_port)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_4)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_7)

        self.jedi_proto = QPushButton(self.centralwidget)
        self.jedi_proto.setObjectName(u"jedi_proto")
        self.jedi_proto.setFont(font1)

        self.verticalLayout_5.addWidget(self.jedi_proto)

        self.ssh_proto = QPushButton(self.centralwidget)
        self.ssh_proto.setObjectName(u"ssh_proto")
        self.ssh_proto.setFont(font1)

        self.verticalLayout_5.addWidget(self.ssh_proto)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_10)

        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.out_display = QTextBrowser(self.centralwidget)
        self.out_display.setObjectName(u"out_display")
        font4 = QFont()
        font4.setFamilies([u"Andale Mono"])
        font4.setPointSize(18)
        font4.setItalic(False)
        self.out_display.setFont(font4)

        self.verticalLayout_4.addWidget(self.out_display)

        self.text_input = QLineEdit(self.centralwidget)
        self.text_input.setObjectName(u"text_input")
        font5 = QFont()
        font5.setFamilies([u"Andale Mono"])
        font5.setItalic(False)
        self.text_input.setFont(font5)

        self.verticalLayout_4.addWidget(self.text_input)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 3, 1, 1, 1)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_9, 9, 2, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 7, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        self.label_7.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_7)

        self.target_host = QComboBox(self.centralwidget)
        self.target_host.setObjectName(u"target_host")
        self.target_host.setEnabled(False)
        self.target_host.setMinimumSize(QSize(180, 0))

        self.horizontalLayout_5.addWidget(self.target_host)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)
        self.label_8.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.target_port = QSpinBox(self.centralwidget)
        self.target_port.setObjectName(u"target_port")
        self.target_port.setEnabled(False)
        self.target_port.setMinimumSize(QSize(80, 0))
        self.target_port.setMinimum(1)
        self.target_port.setMaximum(9999)
        self.target_port.setValue(22)

        self.horizontalLayout_5.addWidget(self.target_port)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.gridLayout.addLayout(self.horizontalLayout_5, 8, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.gridLayout.addLayout(self.horizontalLayout_4, 10, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 1, 1, 1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 9, 1, 1, 1)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_8, 7, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 775, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Disable", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Host", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Port", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"JEDI", None))
        self.label_13.setText(QCoreApplication.translate(
            "MainWindow", u"Remote", None))
        self.label_3.setText(QCoreApplication.translate(
            "MainWindow", u"Host", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Port", None))
        self.jedi_proto.setText(QCoreApplication.translate(
            "MainWindow", u"JEDI PROTOCOL", None))
        self.ssh_proto.setText(QCoreApplication.translate(
            "MainWindow", u"SSH Connect", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Made by: ", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Skywalker", None))
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Next", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"Target", None))
        self.pushButton.setText(QCoreApplication.translate(
            "MainWindow", u"Enable", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Host", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Port", None))
        self.pushButton_3.setText(QCoreApplication.translate(
            "MainWindow", u"Initiate Node", None))
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"Sequence Settings", None))
    # retranslateUi
