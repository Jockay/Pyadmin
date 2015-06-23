# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process.ui'
#
# Created: Thu Mar 26 10:25:00 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *

class Process(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(372, 416)
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setGeometry(QRect(10, 20, 351, 321))
        self.listWidget.setObjectName("listWidget")
        self.pb_new = QPushButton(Dialog)
        self.pb_new.setGeometry(QRect(20, 340, 95, 24))
        self.pb_new.setObjectName("pb_new")
        self.pb_kill = QPushButton(Dialog)
        self.pb_kill.setGeometry(QRect(260, 340, 95, 24))
        self.pb_kill.setObjectName("pb_kill")
        self.pb_close = QPushButton(Dialog)
        self.pb_close.setGeometry(QRect(10, 380, 351, 24))
        self.pb_close.setObjectName("pb_close")
        self.lb_processes = QLabel(Dialog)
        self.lb_processes.setGeometry(QRect(7, 0, 351, 20))
        self.lb_processes.setAlignment(Qt.AlignCenter)
        self.lb_processes.setObjectName("lb_processes")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None, QApplication.UnicodeUTF8))
        self.pb_new.setText(QApplication.translate("Dialog", "New", None, QApplication.UnicodeUTF8))
        self.pb_kill.setText(QApplication.translate("Dialog", "Kill", None, QApplication.UnicodeUTF8))
        self.pb_close.setText(QApplication.translate("Dialog", "Close", None, QApplication.UnicodeUTF8))
        self.lb_processes.setText(QApplication.translate("Dialog", "Running processes", None, QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Process()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

