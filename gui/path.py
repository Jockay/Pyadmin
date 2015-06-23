# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'path.ui'
#
# Created: Wed Mar 25 19:36:20 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class Path(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(347, 114)
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(20, 80, 95, 24))
        self.pb_close.setObjectName("pb_close")
        self.pb_apply = QPushButton(Dialog)
        self.pb_apply.setGeometry(QRect(230, 80, 95, 24))
        self.pb_apply.setObjectName("pb_apply")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(20, 30, 58, 15))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QRect(90, 10, 241, 61))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.pb_apply.setText(QApplication.translate("Dialog", "Apply", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("Dialog", "Path:", None, QApplication.UnicodeUTF8))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Path()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())