# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window (2).ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import roflan

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1454, 610)
        MainWindow.setTabletTracking(True)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setStyleSheet(u"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:#7e74a6")
        self.path_txt = QTextEdit(self.centralwidget)
        self.path_txt.setObjectName(u"path_txt")
        self.path_txt.setGeometry(QRect(400, 30, 291, 31))
        font = QFont()
        font.setPointSize(12)
        self.path_txt.setFont(font)
        self.path_txt.setStyleSheet(u"background-color: #fff;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 391, 31))
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #FFFFFF;\n"
"background-color: #69608a;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 190, 741, 41))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #FFFFFF;\n"
"background-color: #69608a;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(490, 420, 261, 91))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.button.setFont(font2)
        self.button.setStyleSheet(u"background-color: #fff;\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 140, 391, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: #FFFFFF;\n"
"background-color: #69608a;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.directory_btn = QPushButton(self.centralwidget)
        self.directory_btn.setObjectName(u"directory_btn")
        self.directory_btn.setGeometry(QRect(700, 30, 51, 31))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setKerning(True)
        self.directory_btn.setFont(font3)
        self.directory_btn.setStyleSheet(u"background-color: #fff;\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 260, 261, 31))
        font4 = QFont()
        font4.setPointSize(16)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color:#ffffff")
        self.label_4.setLineWidth(4)
        self.info_txt = QTextEdit(self.centralwidget)
        self.info_txt.setObjectName(u"info_txt")
        self.info_txt.setEnabled(False)
        self.info_txt.setGeometry(QRect(400, 250, 351, 41))
        self.info_txt.setFont(font)
        self.info_txt.setStyleSheet(u"background-color: #fff;\n"
"")
        self.info_txt.setFrameShape(QFrame.StyledPanel)
        self.login = QRadioButton(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(10, 250, 181, 41))
        self.login.setFont(font4)
        self.login.setStyleSheet(u"color: #FFFFFF;\n"
"background-color: #69608a;")
        self.time = QRadioButton(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(10, 310, 181, 41))
        self.time.setFont(font4)
        self.time.setStyleSheet(u"color: #FFFFFF;\n"
"background-color: #69608a;")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QRect(10, 530, 1441, 23))
        self.progressBar.setStyleSheet(u"background-color: #fff;\n"
"color: #ffffff\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.elems_cmb = QComboBox(self.centralwidget)
        self.elems_cmb.setObjectName(u"elems_cmb")
        self.elems_cmb.setGeometry(QRect(400, 140, 351, 31))
        self.elems_cmb.setFont(font4)
        self.elems_cmb.setStyleSheet(u"background-color: #fff;\n"
"")
        self.elems_cmb.setCurrentText(u"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 310, 251, 31))
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color:#ffffff")
        self.label_5.setLineWidth(4)
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setEnabled(False)
        self.dateTimeEdit.setGeometry(QRect(400, 310, 351, 41))
        self.dateTimeEdit.setFont(font4)
        self.dateTimeEdit.setStyleSheet(u"background-color: #fff;\n"
"")
        self.dateTimeEdit.setWrapping(False)
        self.dateTimeEdit.setCalendarPopup(True)
        self.anal_btn = QPushButton(self.centralwidget)
        self.anal_btn.setObjectName(u"anal_btn")
        self.anal_btn.setGeometry(QRect(400, 80, 351, 41))
        self.anal_btn.setFont(font2)
        self.anal_btn.setStyleSheet(u"background-color: #fff;\n"
"")
        self.table = QTableWidget(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(760, 10, 681, 501))
        self.table.setStyleSheet(u"background-image:url(:/roflan/roflan.jpg)")
        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(10, 420, 261, 91))
        font5 = QFont()
        font5.setPointSize(14)
        self.save_btn.setFont(font5)
        self.save_btn.setStyleSheet(u"background-color: #fff;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.path_txt.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.button.raise_()
        self.label_3.raise_()
        self.directory_btn.raise_()
        self.label_4.raise_()
        self.info_txt.raise_()
        self.login.raise_()
        self.progressBar.raise_()
        self.elems_cmb.raise_()
        self.label_5.raise_()
        self.dateTimeEdit.raise_()
        self.anal_btn.raise_()
        self.table.raise_()
        self.save_btn.raise_()
        self.time.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1454, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u043f\u0430\u043f\u043a\u0435 \u0441 \u043b\u043e\u0433\u0430\u043c\u0438:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0438\u0434 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438 \u043b\u043e\u0433\u043e\u0432:", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443:", None))
        self.directory_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_4.setText("")
        self.login.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043b\u043e\u0433\u0438\u043d\u0443", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.label_5.setText("")
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy H:mm:ss", None))
        self.anal_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

