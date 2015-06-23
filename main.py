# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Mar 25 19:35:59 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide.QtCore import *
from PySide.QtGui import *
from gui.about_user import AboutUser
from gui.add_repository import AddRepository
from gui.apache_installer import ApacheInstaller
from gui.automatic_installer import AutomaticInstaller
from gui.file_loader import FileLoader
from gui.monitor import Monitor
from gui.mouse import Mouse
from gui.network import Network
from gui.path import Path
from gui.process import Process
from gui.search_file import SearchFile
from gui.sys_activity import SysActivity
from gui.time_and_date import TimeAndDate
from gui.new_process import NewProcess

import sys

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 501)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QRect(10, 10, 521, 431))
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sys_set = QWidget()
        self.tab_sys_set.setObjectName("tab_sys_set")
        # button: About User
        self.pb_user = QPushButton(self.tab_sys_set)
        self.pb_user.setGeometry(QRect(30, 20, 171, 41))
        self.pb_user.setObjectName("pb_user")
        # button: Path
        self.pb_path = QPushButton(self.tab_sys_set)
        self.pb_path.setGeometry(QRect(30, 70, 171, 41))
        self.pb_path.setObjectName("pb_path")
        # button: Mouse
        self.pb_mouse = QPushButton(self.tab_sys_set)
        self.pb_mouse.setGeometry(QRect(30, 120, 171, 41))
        self.pb_mouse.setObjectName("pb_mouse")
        # button: Network
        self.pb_network = QPushButton(self.tab_sys_set)
        self.pb_network.setGeometry(QRect(30, 170, 171, 41))
        self.pb_network.setObjectName("pb_network")
        # button: Time And Date
        self.pb_time_date = QPushButton(self.tab_sys_set)
        self.pb_time_date.setGeometry(QRect(310, 20, 171, 41))
        self.pb_time_date.setObjectName("ps_time_date")
        self.pb_time_date.clicked.connect(self.openTimeAndDate) ##############################
        # button: Computer and System
        self.pb_com_sys = QPushButton(self.tab_sys_set)
        self.pb_com_sys.setGeometry(QRect(310, 70, 171, 41))
        self.pb_com_sys.setObjectName("pb_com_sys")
        # button: Monitor
        self.pb_monitor = QPushButton(self.tab_sys_set)
        self.pb_monitor.setGeometry(QRect(310, 120, 171, 41))
        self.pb_monitor.setObjectName("pb_monitor")
        # button: Search File
        self.pb_search = QPushButton(self.tab_sys_set)
        self.pb_search.setGeometry(QRect(310, 170, 171, 41))
        self.pb_search.setObjectName("pb_search")
        # button: Tasks
        self.pb_tasks = QPushButton(self.tab_sys_set)
        self.pb_tasks.setGeometry(QRect(30, 300, 171, 41))
        self.pb_tasks.setObjectName("pb_tasks")
        # button: System Activity
        self.pb_sys_activity = QPushButton(self.tab_sys_set)
        self.pb_sys_activity.setGeometry(QRect(30, 350, 171, 41))
        self.pb_sys_activity.setObjectName("pb_sys_activity")
        self.lb_memorymb = QLabel(self.tab_sys_set)
        self.lb_memorymb.setGeometry(QRect(390, 360, 91, 20))
        self.lb_memorymb.setAlignment(Qt.AlignCenter)
        self.lb_memorymb.setObjectName("lb_memorymb")
        self.lb_free_memory = QLabel(self.tab_sys_set)
        self.lb_free_memory.setGeometry(QRect(300, 360, 91, 16))
        self.lb_free_memory.setObjectName("lb_free_memory")
        self.label = QLabel(self.tab_sys_set)
        self.label.setGeometry(QRect(490, 360, 21, 20))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_sys_set, "")
        self.tab_installer = QWidget()
        self.tab_installer.setObjectName("tab_installer")
        self.lineEdit = QLineEdit(self.tab_installer)
        self.lineEdit.setGeometry(QRect(20, 10, 371, 23))
        self.lineEdit.setObjectName("lineEdit")
        # button: Search in repository
        self.pb_search_repo = QPushButton(self.tab_installer)
        self.pb_search_repo.setGeometry(QRect(400, 10, 91, 24))
        self.pb_search_repo.setObjectName("pb_search_repo")
        # button: Add repository
        self.pb_add_repo = QPushButton(self.tab_installer)
        self.pb_add_repo.setGeometry(QRect(20, 370, 221, 24))
        self.pb_add_repo.setObjectName("pb_add_repo")
        # button: Autoinstall
        self.pb_autoinstall = QPushButton(self.tab_installer)
        self.pb_autoinstall.setGeometry(QRect(260, 370, 231, 24))
        self.pb_autoinstall.setObjectName("pb_autoinstall")
        self.listWidget = QListWidget(self.tab_installer)
        self.listWidget.setGeometry(QRect(20, 40, 471, 321))
        self.listWidget.setObjectName("listWidget")
        self.lb_pname_example = QLabel(self.tab_installer)
        self.lb_pname_example.setGeometry(QRect(30, 50, 231, 16))
        self.lb_pname_example.setObjectName("lb_pname_example")
        # button: Install/Uninstall
        self.pb_install_uninstall = QPushButton(self.tab_installer)
        self.pb_install_uninstall.setGeometry(QRect(364, 50, 111, 24))
        self.pb_install_uninstall.setObjectName("pb_install_uninstall")
        self.tabWidget.addTab(self.tab_installer, "")
        self.lb_username = QLabel(self.centralwidget)
        self.lb_username.setGeometry(QRect(10, 440, 211, 16))
        self.lb_username.setObjectName("lb_username")
        self.lb_uptime = QLabel(self.centralwidget)
        self.lb_uptime.setGeometry(QRect(300, 440, 231, 20))
        self.lb_uptime.setLayoutDirection(Qt.RightToLeft)
        self.lb_uptime.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lb_uptime.setObjectName("lb_uptime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        self.menuApplication = QMenu(self.menubar)
        self.menuApplication.setObjectName("menuApplication")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLanguage = QAction(MainWindow)
        self.actionLanguage.setObjectName("actionLanguage")
        self.actionButton_Functions_Help = QAction(MainWindow)
        self.actionButton_Functions_Help.setObjectName("actionButton_Functions_Help")
        self.actionAbout_Author = QAction(MainWindow)
        self.actionAbout_Author.setObjectName("actionAbout_Author")
        self.actionConfigure_and_Install_Apache_Server = QAction(MainWindow)
        self.actionConfigure_and_Install_Apache_Server.setObjectName("actionConfigure_and_Install_Apache_Server")
        self.actionUpdate_Packages = QAction(MainWindow)
        self.actionUpdate_Packages.setObjectName("actionUpdate_Packages")
        self.menuApplication.addAction(self.actionLanguage)
        self.menuApplication.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionButton_Functions_Help)
        self.menuHelp.addAction(self.actionAbout_Author)
        self.menuTools.addAction(self.actionConfigure_and_Install_Apache_Server)
        self.menuTools.addAction(self.actionUpdate_Packages)
        self.menubar.addAction(self.menuApplication.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "PyAdmin", None, QApplication.UnicodeUTF8))
        self.pb_user.setText(QApplication.translate("MainWindow", "About User", None, QApplication.UnicodeUTF8))
        self.pb_path.setText(QApplication.translate("MainWindow", "Configure Path", None, QApplication.UnicodeUTF8))
        self.pb_mouse.setText(QApplication.translate("MainWindow", "Mouse", None, QApplication.UnicodeUTF8))
        self.pb_network.setText(QApplication.translate("MainWindow", "Network", None, QApplication.UnicodeUTF8))
        self.pb_time_date.setText(QApplication.translate("MainWindow", "Time and Date", None, QApplication.UnicodeUTF8))
        self.pb_com_sys.setText(QApplication.translate("MainWindow", "Computer and System", None, QApplication.UnicodeUTF8))
        self.pb_monitor.setText(QApplication.translate("MainWindow", "Monitor", None, QApplication.UnicodeUTF8))
        self.pb_search.setText(QApplication.translate("MainWindow", "Search File", None, QApplication.UnicodeUTF8))
        self.pb_tasks.setText(QApplication.translate("MainWindow", "Manage Tasks", None, QApplication.UnicodeUTF8))
        self.pb_sys_activity.setText(QApplication.translate("MainWindow", "View System Activity", None, QApplication.UnicodeUTF8))
        self.lb_memorymb.setText(QApplication.translate("MainWindow", "0", None, QApplication.UnicodeUTF8))
        self.lb_free_memory.setText(QApplication.translate("MainWindow", "Free Memory:", None, QApplication.UnicodeUTF8))
        self.label.setText(QApplication.translate("MainWindow", "mb", None, QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sys_set), QApplication.translate("MainWindow", "System Settings", None, QApplication.UnicodeUTF8))
        self.pb_search_repo.setText(QApplication.translate("MainWindow", "Search", None, QApplication.UnicodeUTF8))
        self.pb_add_repo.setText(QApplication.translate("MainWindow", "Add Repository", None, QApplication.UnicodeUTF8))
        self.pb_autoinstall.setText(QApplication.translate("MainWindow", "Automatic Installer", None, QApplication.UnicodeUTF8))
        self.lb_pname_example.setText(QApplication.translate("MainWindow", "Package Name", None, QApplication.UnicodeUTF8))
        self.pb_install_uninstall.setText(QApplication.translate("MainWindow", "Install / Remove", None, QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_installer), QApplication.translate("MainWindow", "Installer", None, QApplication.UnicodeUTF8))
        self.lb_username.setText(QApplication.translate("MainWindow", "Username", None, QApplication.UnicodeUTF8))
        self.lb_uptime.setText(QApplication.translate("MainWindow", "Uptime", None, QApplication.UnicodeUTF8))
        self.menuApplication.setTitle(QApplication.translate("MainWindow", "Application", None, QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QApplication.translate("MainWindow", "Help", None, QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QApplication.translate("MainWindow", "Tools", None, QApplication.UnicodeUTF8))
        self.actionExit.setText(QApplication.translate("MainWindow", "Exit", None, QApplication.UnicodeUTF8))
        self.actionLanguage.setText(QApplication.translate("MainWindow", "Language", None, QApplication.UnicodeUTF8))
        self.actionButton_Functions_Help.setText(QApplication.translate("MainWindow", "About Buttons", None, QApplication.UnicodeUTF8))
        self.actionAbout_Author.setText(QApplication.translate("MainWindow", "About Author", None, QApplication.UnicodeUTF8))
        self.actionConfigure_and_Install_Apache_Server.setText(QApplication.translate("MainWindow", "Configure and Install Apache Server", None, QApplication.UnicodeUTF8))
        self.actionUpdate_Packages.setText(QApplication.translate("MainWindow", "Update Packages", None, QApplication.UnicodeUTF8))

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        # self.connect(self.pb_user, Signal("clicked()"), self.openAboutUser())
        # self.connect(self.pb_add_repo, Signal("clicked()"), self.openAddRepository())
        # self.connect(self.actionConfigure_and_Install_Apache_Server, Signal("clicked()"), self.openApacheInstaller())
        # self.connect(self.pb_autoinstall, Signal("clicked()"), self.openAutomaticInstaller())
        # self.connect(self.pb_monitor, Signal("clicked()"), self.openMonitor())
        # self.connect(self.pb_time_date, Signal("clicked()"), self.openTimeAndDate())

    def openAboutUser(self):
        frame = AboutUser()
        frame.exec_()

    def openAddRepository(self):
        frame = AddRepository()
        frame.exec_()

    def openApacheInstaller(self):
        frame = ApacheInstaller()
        frame.exec_()

    def openAutomaticInstaller(self):
        frame = AutomaticInstaller()
        frame.exec_()

    def openFileLoader(self):
        frame = FileLoader()
        frame.exec_()

    def openMonitor(self):
        frame = Monitor()
        frame.exec_()

    def openMouse(self):
        frame = Mouse()
        frame.exec_()

    def openNetwork(self):
        frame = Network()
        frame.exec_()

    def openNewProcess(self):
        frame = NewProcess()
        frame.exec_()

    def openPath(self):
        frame = Path()
        frame.exec_()

    def openProcess(self):
        frame = Process()
        frame.exec_()

    def openSearchFile(self):
        frame = SearchFile()
        frame.exec_()

    def openSysActivity(self):
        frame = SysActivity()
        frame.exec_()

    def openTimeAndDate(self):
        print "It works"
        #frame = TimeAndDate()
        Form = QWidget()
        ui = TimeAndDate()
        ui.setupUi(Form)
        Form.show()
        #sys.exit(app.exec_())

#class ControlMainWindow(QMainWindow):
#    def __init__(self, parent=None):
#        super(ControlMainWindow, self).__init__(parent)
#        self.ui = Ui_MainWindow()
#        self.ui.setupUi(self)

#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    mainWindow = Ui_MainWindow()
#    mainWindow.show()
#    mainWindowContoller = ControlMainWindow()
#    mainWindowContoller.show()
#    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
