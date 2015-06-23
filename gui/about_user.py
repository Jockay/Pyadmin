# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_user.ui'
#
# Created: Wed Mar 25 19:33:06 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *


class AboutUser(object):
    def __init__(self):
        super(AboutUser, self).__init__()
        # self.setupUi(self)
        # self.retranslateUi(self)
        # self.setupUi(self)
        # self.retranslateUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("dw_about_user")
        Dialog.resize(392, 157)
        self.le_username = QLineEdit(Dialog)
        self.le_username.setGeometry(QRect(250, 20, 121, 23))
        self.le_username.setObjectName("le_username")
        self.lb_username = QLabel(Dialog)
        self.lb_username.setGeometry(QRect(180, 20, 71, 20))
        self.lb_username.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_username.setObjectName("lb_username")
        self.lb_passwd = QLabel(Dialog)
        self.lb_passwd.setGeometry(QRect(180, 40, 71, 20))
        self.lb_passwd.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_passwd.setObjectName("lb_passwd")
        self.lb_passwd_again = QLabel(Dialog)
        self.lb_passwd_again.setGeometry(QRect(150, 60, 101, 20))
        self.lb_passwd_again.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_passwd_again.setObjectName("lb_passwd_again")
        self.le_passwd = QLineEdit(Dialog)
        self.le_passwd.setGeometry(QRect(250, 40, 121, 23))
        self.le_passwd.setObjectName("lineEdit")
        self.le_passwd_again = QLineEdit(Dialog)
        self.le_passwd_again.setGeometry(QRect(250, 60, 121, 23))
        self.le_passwd_again.setObjectName("lineEdit_2")
        self.pb_avatar = QPushButton(Dialog)
        self.pb_avatar.setGeometry(QRect(20, 10, 111, 81))
        self.pb_avatar.setObjectName("pb_avatar")
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(30, 120, 95, 24))
        self.pb_close.setObjectName("pb_close")
        self.pb_apply = QPushButton(Dialog)
        self.pb_apply.setGeometry(QRect(280, 120, 95, 24))
        self.pb_apply.setObjectName("pb_apply")
        self.lb_clicktochange = QLabel(Dialog)
        self.lb_clicktochange.setGeometry(QRect(20, 90, 111, 20))
        self.lb_clicktochange.setAlignment(Qt.AlignCenter)
        self.lb_clicktochange.setObjectName("lb_clicktochange")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, dw_about_user):
        dw_about_user.setWindowTitle(QApplication.translate("dw_about_user", "About User", None, QApplication.UnicodeUTF8))
        self.lb_username.setText(QApplication.translate("dw_about_user", "Username:", None, QApplication.UnicodeUTF8))
        self.lb_passwd.setText(QApplication.translate("dw_about_user", "Password:", None, QApplication.UnicodeUTF8))
        self.lb_passwd_again.setText(QApplication.translate("dw_about_user", "Password again:", None, QApplication.UnicodeUTF8))
        self.pb_avatar.setText(QApplication.translate("dw_about_user", "Picture", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("dw_about_user", "Close", None, QApplication.UnicodeUTF8))
        self.pb_apply.setText(QApplication.translate("dw_about_user", "Apply", None, QApplication.UnicodeUTF8))
        self.lb_clicktochange.setText(QApplication.translate("dw_about_user", "(click to change)", None, QApplication.UnicodeUTF8))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = AboutUser()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())