# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_repository.ui'
#
# Created: Wed Mar 25 19:33:49 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *


class AddRepository(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 199)
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(20, 10, 131, 16))
        self.label.setObjectName("label")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setGeometry(QRect(20, 30, 261, 91))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(20, 120, 261, 24))
        self.pushButton.setObjectName("pushButton")
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(20, 160, 95, 24))
        self.pb_close.setObjectName("pb_close")
        self.pb_add = QPushButton(Dialog)
        self.pb_add.setGeometry(QRect(190, 160, 95, 24))
        self.pb_add.setObjectName("pb_add")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("Dialog", "Repositories to add:", None, QApplication.UnicodeUTF8))
        self.pushButton.setText(QApplication.translate("Dialog", "Load file by url", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.pb_add.setText(QApplication.translate("Dialog", "Add", None, QApplication.UnicodeUTF8))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = AddRepository()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())