# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'time_and_date.ui'
#
# Created: Wed Mar 25 19:39:24 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *


class TimeAndDate(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(347, 139)
        self.lb_time = QLabel(Dialog)
        self.lb_time.setGeometry(QRect(50, 20, 91, 20))
        self.lb_time.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_time.setObjectName("lb_time")
        self.lb_date = QLabel(Dialog)
        self.lb_date.setGeometry(QRect(17, 60, 121, 20))
        self.lb_date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lb_date.setObjectName("lb_date")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(150, 20, 51, 23))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lb_dd = QLabel(Dialog)
        self.lb_dd.setGeometry(QRect(200, 20, 21, 16))
        self.lb_dd.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.lb_dd.setObjectName("lb_dd")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QRect(220, 20, 51, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(30, 100, 95, 24))
        self.pb_close.setObjectName("pb_close")
        self.pb_apply = QPushButton(Dialog)
        self.pb_apply.setGeometry(QRect(220, 100, 95, 24))
        self.pb_apply.setObjectName("pb_apply")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QRect(150, 60, 61, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QRect(230, 60, 41, 23))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QRect(290, 60, 41, 23))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lb_slash1 = QLabel(Dialog)
        self.lb_slash1.setGeometry(QRect(210, 60, 21, 21))
        self.lb_slash1.setAlignment(Qt.AlignCenter)
        self.lb_slash1.setObjectName("lb_slash1")
        self.lb_slash2 = QLabel(Dialog)
        self.lb_slash2.setGeometry(QRect(270, 60, 21, 21))
        self.lb_slash2.setAlignment(Qt.AlignCenter)
        self.lb_slash2.setObjectName("lb_slash2")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.lb_time.setText(QApplication.translate("Dialog", "Time (HH:MM)", None, QApplication.UnicodeUTF8))
        self.lb_date.setText(QApplication.translate("Dialog", "Date (YYYY/MM/DD)", None, QApplication.UnicodeUTF8))
        self.lb_dd.setText(QApplication.translate("Dialog", ":", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.pb_apply.setText(QApplication.translate("Dialog", "Apply", None, QApplication.UnicodeUTF8))
        self.lb_slash1.setText(QApplication.translate("Dialog", "/", None, QApplication.UnicodeUTF8))
        self.lb_slash2.setText(QApplication.translate("Dialog", "/", None, QApplication.UnicodeUTF8))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = TimeAndDate()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())