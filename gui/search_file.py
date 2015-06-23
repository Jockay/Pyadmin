# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_file.ui'
#
# Created: Thu Mar 26 11:05:20 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class SearchFile(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(402, 407)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(30, 10, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(30, 40, 101, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(130, 10, 241, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QRect(130, 40, 241, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setGeometry(QRect(30, 100, 341, 251))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(30, 70, 341, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setGeometry(QRect(30, 370, 341, 24))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("Dialog", "Path to search", None, QApplication.UnicodeUTF8))
        self.label_2.setText(QApplication.translate("Dialog", "Name to search", None, QApplication.UnicodeUTF8))
        self.pushButton.setText(QApplication.translate("Dialog", "Start", None, QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = SearchFile()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

