# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainwindow.ui.autosave'
##
# Created by: Qt User Interface Compiler version 6.5.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
                               QHBoxLayout, QLabel, QLayout, QLineEdit,
                               QMainWindow, QMenu, QMenuBar, QPushButton,
                               QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
                               QTabWidget, QTextBrowser, QVBoxLayout, QWidget)


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(714, 645)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(51, 51, 51, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(76, 76, 76, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(63, 63, 63, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(25, 25, 25, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(34, 34, 34, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 127))
        brush8.setStyle(Qt.SolidPattern)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
# endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
# endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(25, 25, 25, 127))
        brush9.setStyle(Qt.SolidPattern)
# if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
# endif
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setBaseSize(QSize(0, 0))
        palette1 = QPalette()
        brush10 = QBrush(QColor(153, 153, 153, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        self.label.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Galvji"])
        font.setPointSize(41)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(32, 32))
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(False)
        font1 = QFont()
        font1.setFamilies([u"Gill Sans"])
        self.label_10.setFont(font1)

        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)

        self.lastnode_check = QCheckBox(self.tab)
        self.lastnode_check.setObjectName(u"lastnode_check")
        self.lastnode_check.setLayoutDirection(Qt.RightToLeft)
        self.lastnode_check.setAutoFillBackground(False)
        self.lastnode_check.setTristate(False)

        self.gridLayout_6.addWidget(self.lastnode_check, 2, 1, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(False)
        font2 = QFont()
        font2.setFamilies([u"Gill Sans"])
        font2.setPointSize(25)
        self.label_9.setFont(font2)

        self.gridLayout_6.addWidget(self.label_9, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.next_label = QLabel(self.tab)
        self.next_label.setObjectName(u"next_label")

        self.horizontalLayout_2.addWidget(self.next_label)

        self.next_ip_cmb = QComboBox(self.tab)
        self.next_ip_cmb.addItem("")
        self.next_ip_cmb.setObjectName(u"next_ip_cmb")
        self.next_ip_cmb.setMinimumSize(QSize(200, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush11 = QBrush(QColor(102, 102, 102, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush11)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush11)
        self.next_ip_cmb.setPalette(palette2)

        self.horizontalLayout_2.addWidget(self.next_ip_cmb)

        self.next_port_label = QLabel(self.tab)
        self.next_port_label.setObjectName(u"next_port_label")

        self.horizontalLayout_2.addWidget(self.next_port_label)

        self.next_port_spin = QSpinBox(self.tab)
        self.next_port_spin.setObjectName(u"next_port_spin")
        self.next_port_spin.setMinimum(1)
        self.next_port_spin.setMaximum(9999)
        self.next_port_spin.setValue(23)

        self.horizontalLayout_2.addWidget(self.next_port_spin)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.initiate_btn = QPushButton(self.tab)
        self.initiate_btn.setObjectName(u"initiate_btn")

        self.verticalLayout.addWidget(self.initiate_btn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_ip = QLabel(self.tab)
        self.label_ip.setObjectName(u"label_ip")
        self.label_ip.setEnabled(False)

        self.horizontalLayout.addWidget(self.label_ip)

        self.target_ip_line_edit = QLineEdit(self.tab)
        self.target_ip_line_edit.setObjectName(u"target_ip_line_edit")
        self.target_ip_line_edit.setEnabled(False)

        self.horizontalLayout.addWidget(self.target_ip_line_edit)

        self.label_port = QLabel(self.tab)
        self.label_port.setObjectName(u"label_port")
        self.label_port.setEnabled(False)

        self.horizontalLayout.addWidget(self.label_port)

        self.target_port_spin = QSpinBox(self.tab)
        self.target_port_spin.setObjectName(u"target_port_spin")
        self.target_port_spin.setEnabled(False)
        self.target_port_spin.setMinimumSize(QSize(90, 0))
        self.target_port_spin.setMinimum(1)
        self.target_port_spin.setMaximum(9999)
        self.target_port_spin.setValue(22)

        self.horizontalLayout.addWidget(self.target_port_spin)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout_6.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.text_out = QTextBrowser(self.tab)
        self.text_out.setObjectName(u"text_out")
        self.text_out.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.text_out.setOpenLinks(False)

        self.gridLayout_5.addWidget(self.text_out, 1, 0, 1, 1)

        self.ping_btn = QPushButton(self.tab)
        self.ping_btn.setObjectName(u"ping_btn")

        self.gridLayout_5.addWidget(self.ping_btn, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.text_in = QLineEdit(self.tab)
        self.text_in.setObjectName(u"text_in")
        font3 = QFont()
        font3.setFamilies([u"Gill Sans"])
        font3.setPointSize(14)
        self.text_in.setFont(font3)
        self.text_in.setCursor(QCursor(Qt.IBeamCursor))

        self.horizontalLayout_4.addWidget(self.text_in)

        self.gridLayout_5.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.settings_label = QLabel(self.tab)
        self.settings_label.setObjectName(u"settings_label")
        font4 = QFont()
        font4.setFamilies([u"Galvji"])
        font4.setPointSize(13)
        font4.setBold(False)
        font4.setItalic(False)
        self.settings_label.setFont(font4)
        self.settings_label.setScaledContents(False)
        self.settings_label.setAlignment(Qt.AlignCenter)
        self.settings_label.setMargin(10)

        self.gridLayout_4.addWidget(self.settings_label, 0, 0, 1, 1)

        self.port_spin = QSpinBox(self.tab)
        self.port_spin.setObjectName(u"port_spin")
        self.port_spin.setAlignment(Qt.AlignCenter)
        self.port_spin.setMinimum(1)
        self.port_spin.setMaximum(9999)
        self.port_spin.setValue(21)

        self.gridLayout_4.addWidget(self.port_spin, 4, 0, 1, 1)

        self.ip_cmb = QComboBox(self.tab)
        self.ip_cmb.addItem("")
        self.ip_cmb.setObjectName(u"ip_cmb")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush11)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush11)
        self.ip_cmb.setPalette(palette3)

        self.gridLayout_4.addWidget(self.ip_cmb, 2, 0, 1, 1)

        self.ip_label = QLabel(self.tab)
        self.ip_label.setObjectName(u"ip_label")
        font5 = QFont()
        font5.setFamilies([u"Futura"])
        self.ip_label.setFont(font5)
        self.ip_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ip_label, 1, 0, 1, 1)

        self.port_label = QLabel(self.tab)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setFont(font5)
        self.port_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.port_label, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.ssh_conn = QPushButton(self.tab)
        self.ssh_conn.setObjectName(u"ssh_conn")

        self.gridLayout_4.addWidget(self.ssh_conn, 7, 0, 1, 1)

        self.pnp_conn = QPushButton(self.tab)
        self.pnp_conn.setObjectName(u"pnp_conn")

        self.gridLayout_4.addWidget(self.pnp_conn, 6, 0, 1, 1)

        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        icon = QIcon()
        iconThemeName = u"battery"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget = QWidget(self.tab_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, -10, 691, 491))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.enter_tab_name = QLineEdit(self.gridLayoutWidget)
        self.enter_tab_name.setObjectName(u"enter_tab_name")

        self.gridLayout_7.addWidget(self.enter_tab_name, 0, 0, 1, 1)

        icon1 = QIcon()
        iconThemeName = u"computer"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.tabWidget.addTab(self.tab_2, icon1, "")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 714, 24))
        self.menuSkywalker = QMenu(self.menubar)
        self.menuSkywalker.setObjectName(u"menuSkywalker")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuSkywalker.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Proxy Nodes</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Made by:", None))
        self.lastnode_check.setText(
            QCoreApplication.translate("MainWindow", u"Last node", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Skywalker", None))
        self.next_label.setText(QCoreApplication.translate(
            "MainWindow", u"Next Node (IPv4): ", None))
        self.next_ip_cmb.setItemText(
            0, QCoreApplication.translate("MainWindow", u"127.0.0.1", None))

        self.next_port_label.setText(QCoreApplication.translate(
            "MainWindow", u"Node Port: ", None))
        self.initiate_btn.setText(QCoreApplication.translate(
            "MainWindow", u"Initiate Node", None))
        self.label_ip.setText(QCoreApplication.translate(
            "MainWindow", u"Target Host: ", None))
        self.label_port.setText(QCoreApplication.translate(
            "MainWindow", u"Target Port: ", None))
        self.ping_btn.setText(QCoreApplication.translate(
            "MainWindow", u"Ping", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">CLI:</span></p></body></html>", None))
        self.text_in.setText("")
        self.text_in.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"type command here...", None))
        self.settings_label.setText(QCoreApplication.translate(
            "MainWindow", u"Remote settings", None))
        self.ip_cmb.setItemText(0, QCoreApplication.translate(
            "MainWindow", u"127.0.0.1", None))

        self.ip_label.setText(QCoreApplication.translate(
            "MainWindow", u"IPv4", None))
        self.port_label.setText(
            QCoreApplication.translate("MainWindow", u"Port", None))
        self.ssh_conn.setText(QCoreApplication.translate(
            "MainWindow", u"SSH Connect", None))
        self.pnp_conn.setText(QCoreApplication.translate(
            "MainWindow", u"PNP Connect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), QCoreApplication.translate("MainWindow", u"Init", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), QCoreApplication.translate("MainWindow", u"NEW", None))
        self.menuSkywalker.setTitle(
            QCoreApplication.translate("MainWindow", u"Skywalker", None))
    # retranslateUi
