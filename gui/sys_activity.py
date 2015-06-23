# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sys_activity.ui'
#
# Created: Thu Mar 26 11:05:08 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class SysActivity(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 428)
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(10, 390, 411, 24))
        self.pb_close.setObjectName("pb_close")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setGeometry(QRect(10, 30, 411, 351))
        self.textEdit.setObjectName("textEdit")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(20, 10, 391, 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("Dialog", "System Activity", None, QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = SysActivity()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

