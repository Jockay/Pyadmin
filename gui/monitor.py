# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor.ui'
#
# Created: Wed Mar 25 19:34:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *
import sys
import modules.monitor as m

class Monitor(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(306, 151)
        self.lb_resolution = QLabel(Dialog)
        self.lb_resolution.setGeometry(QRect(20, 20, 81, 21))
        self.lb_resolution.setObjectName("lb_resolution")
        self.lb_x = QLabel(Dialog)
        self.lb_x.setGeometry(QRect(180, 20, 21, 21))
        self.lb_x.setAlignment(Qt.AlignCenter)
        self.lb_x.setObjectName("lb_x")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setGeometry(QRect(110, 20, 71, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QRect(200, 20, 71, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lb_redreshrate = QLabel(Dialog)
        self.lb_redreshrate.setGeometry(QRect(20, 70, 91, 17))
        self.lb_redreshrate.setObjectName("lb_redreshrate")
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QRect(110, 70, 51, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        # button: close window
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(20, 110, 95, 24))
        self.pb_close.setObjectName("pb_close")
        self.pb_close.click(sys.exit(0))
        # button: apply
        self.pb_apply = QPushButton(Dialog)
        self.pb_apply.setGeometry(QRect(180, 110, 95, 24))
        self.pb_apply.setObjectName("pushButton_2")
        #resolution=
        # label: hertz number
        self.lb_hz = QLabel(Dialog)
        self.lb_hz.setGeometry(QRect(170, 70, 21, 21))
        self.lb_hz.setObjectName("lb_hz")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.lb_resolution.setText(QApplication.translate("Dialog", "Resolution", None, QApplication.UnicodeUTF8))
        self.lb_x.setText(QApplication.translate("Dialog", "x", None, QApplication.UnicodeUTF8))
        self.lb_redreshrate.setText(QApplication.translate("Dialog", "Refresh rate", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.pb_apply.setText(QApplication.translate("Dialog", "Apply", None, QApplication.UnicodeUTF8))
        self.lb_hz.setText(QApplication.translate("Dialog", "hz", None, QApplication.UnicodeUTF8))

    def set_monitor(self, resolution="", refresh_rate=""):
        m.set_resolution(resolution)
        m.set_refresh_rate(refresh_rate)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Monitor()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())