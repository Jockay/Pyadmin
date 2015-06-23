# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_process.ui'
#
# Created: Thu Mar 26 10:25:27 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class NewProcess(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 134)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(20, 10, 281, 20))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(40, 40, 241, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(30, 80, 95, 24))
        self.pb_close.setObjectName("pb_close")
        self.pb_run = QPushButton(Dialog)
        self.pb_run.setGeometry(QRect(200, 80, 95, 24))
        self.pb_run.setObjectName("pb_run")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("Dialog", "New Process", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.pb_run.setText(QApplication.translate("Dialog", "Run", None, QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = NewProcess()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

