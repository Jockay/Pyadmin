# -*- coding: utf-8 -*-

__author__ = 'jockay'

import sys

from PySide.QtGui  import *

import main


class ControlMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = ControlMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())