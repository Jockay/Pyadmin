# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_loader.ui'
#
# Created: Wed Mar 25 19:34:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class FileLoader(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(284, 95)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(20, 50, 95, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setGeometry(QRect(160, 50, 95, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(20, 10, 241, 23))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.pushButton.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QApplication.translate("Dialog", "Load", None, QApplication.UnicodeUTF8))

