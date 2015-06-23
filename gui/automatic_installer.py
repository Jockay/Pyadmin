# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automatic_installer.ui'
#
# Created: Wed Mar 25 19:34:14 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class AutomaticInstaller(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 300)
        self.te_packages = QTextEdit(Dialog)
        self.te_packages.setGeometry(QRect(20, 40, 351, 181))
        self.te_packages.setObjectName("te_packages")
        self.lb_packagestoinstall = QLabel(Dialog)
        self.lb_packagestoinstall.setGeometry(QRect(30, 10, 131, 21))
        self.lb_packagestoinstall.setObjectName("lb_packagestoinstall")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(20, 220, 351, 24))
        self.pushButton.setObjectName("pushButton")
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(20, 260, 95, 24))
        self.pb_close.setObjectName("pb_close")
        self.pb_Start = QPushButton(Dialog)
        self.pb_Start.setGeometry(QRect(280, 260, 95, 24))
        self.pb_Start.setObjectName("pb_Start")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.lb_packagestoinstall.setText(QApplication.translate("Dialog", "Packages to install:", None, QApplication.UnicodeUTF8))
        self.pushButton.setText(QApplication.translate("Dialog", "Load file by path name", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.pb_Start.setText(QApplication.translate("Dialog", "Start", None, QApplication.UnicodeUTF8))

