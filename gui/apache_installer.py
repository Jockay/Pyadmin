# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apache_installer.ui'
#
# Created: Wed Mar 25 19:35:41 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *


class ApacheInstaller(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(392, 274)
        self.cb_php = QCheckBox(Dialog)
        self.cb_php.setGeometry(QRect(40, 40, 86, 21))
        self.cb_php.setObjectName("cb_php")
        self.cb_mysql = QCheckBox(Dialog)
        self.cb_mysql.setGeometry(QRect(40, 80, 86, 21))
        self.cb_mysql.setObjectName("cb_mysql")
        self.cb_phpmyadmin = QCheckBox(Dialog)
        self.cb_phpmyadmin.setGeometry(QRect(180, 40, 121, 21))
        self.cb_phpmyadmin.setObjectName("cb_phpmyadmin")
        self.lb_rootpasswd = QLabel(Dialog)
        self.lb_rootpasswd.setGeometry(QRect(150, 80, 91, 21))
        self.lb_rootpasswd.setObjectName("lb_rootpasswd")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(240, 80, 113, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.rb_customport = QRadioButton(Dialog)
        self.rb_customport.setGeometry(QRect(40, 130, 251, 21))
        self.rb_customport.setObjectName("rb_customport")
        self.rb_default_port = QRadioButton(Dialog)
        self.rb_default_port.setGeometry(QRect(40, 190, 131, 21))
        self.rb_default_port.setObjectName("rb_default_port")
        self.lb_installwith = QLabel(Dialog)
        self.lb_installwith.setGeometry(QRect(40, 10, 81, 16))
        self.lb_installwith.setObjectName("lb_installwith")
        self.lb_port = QLabel(Dialog)
        self.lb_port.setGeometry(QRect(70, 154, 91, 31))
        self.lb_port.setObjectName("lb_port")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QRect(160, 160, 113, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(40, 230, 95, 24))
        self.pb_close.setObjectName("pb_close")
        self.pb_start = QPushButton(Dialog)
        self.pb_start.setGeometry(QRect(240, 230, 95, 24))
        self.pb_start.setObjectName("pb_start")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.cb_php.setText(QApplication.translate("Dialog", "PHP", None, QApplication.UnicodeUTF8))
        self.cb_mysql.setText(QApplication.translate("Dialog", "MySQL", None, QApplication.UnicodeUTF8))
        self.cb_phpmyadmin.setText(QApplication.translate("Dialog", "PHP my admin", None, QApplication.UnicodeUTF8))
        self.lb_rootpasswd.setText(QApplication.translate("Dialog", "Root Password: ", None, QApplication.UnicodeUTF8))
        self.rb_customport.setText(QApplication.translate("Dialog", "Configure with custom port number", None, QApplication.UnicodeUTF8))
        self.rb_default_port.setText(QApplication.translate("Dialog", "Use default port", None, QApplication.UnicodeUTF8))
        self.lb_installwith.setText(QApplication.translate("Dialog", "Install with:", None, QApplication.UnicodeUTF8))
        self.lb_port.setText(QApplication.translate("Dialog", "Port Number:", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.pb_start.setText(QApplication.translate("Dialog", "Start", None, QApplication.UnicodeUTF8))

