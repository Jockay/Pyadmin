# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mouse.ui'
#
# Created: Wed Mar 25 19:36:10 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class Mouse(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(252, 266)
        self.lb_cursor_type = QLabel(Dialog)
        self.lb_cursor_type.setGeometry(QRect(20, 40, 71, 21))
        self.lb_cursor_type.setObjectName("lb_cursor_type")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(100, 10, 113, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QRect(100, 40, 113, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lb_cursor_types = QLabel(Dialog)
        self.lb_cursor_types.setGeometry(QRect(20, 80, 151, 16))
        self.lb_cursor_types.setObjectName("lb_cursor_types")
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setGeometry(QRect(10, 100, 231, 101))
        self.listWidget.setObjectName("listWidget")
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(20, 230, 95, 24))
        self.pb_close.setObjectName("pb_close")
        self.pb_apply = QPushButton(Dialog)
        self.pb_apply.setGeometry(QRect(140, 230, 95, 24))
        self.pb_apply.setObjectName("pb_apply")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(20, 10, 71, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.lb_cursor_type.setText(QApplication.translate("Dialog", "Cursor type:", None, QApplication.UnicodeUTF8))
        self.lb_cursor_types.setText(QApplication.translate("Dialog", "Available Cursor Types", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.pb_apply.setText(QApplication.translate("Dialog", "Apply", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("Dialog", "Sensitivity", None, QApplication.UnicodeUTF8))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Mouse()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())