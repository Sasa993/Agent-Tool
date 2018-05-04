# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_fajl.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(581, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../Desktop/saki.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.vrijeme_lbl = QtGui.QLabel(self.centralwidget)
        self.vrijeme_lbl.setObjectName(_fromUtf8("vrijeme_lbl"))
        self.horizontalLayout_2.addWidget(self.vrijeme_lbl)
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setObjectName(_fromUtf8("start"))
        self.horizontalLayout_2.addWidget(self.start)
        self.stop = QtGui.QPushButton(self.centralwidget)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.horizontalLayout_2.addWidget(self.stop)
        self.reset = QtGui.QPushButton(self.centralwidget)
        self.reset.setObjectName(_fromUtf8("reset"))
        self.horizontalLayout_2.addWidget(self.reset)
        spacerItem = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem1 = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_8.addWidget(self.label_2)
        self.prvi_input = QtGui.QLineEdit(self.centralwidget)
        self.prvi_input.setStyleSheet(_fromUtf8(""))
        self.prvi_input.setObjectName(_fromUtf8("prvi_input"))
        self.verticalLayout_8.addWidget(self.prvi_input)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_8.addWidget(self.label)
        self.drugi_input = QtGui.QLineEdit(self.centralwidget)
        self.drugi_input.setStyleSheet(_fromUtf8(""))
        self.drugi_input.setObjectName(_fromUtf8("drugi_input"))
        self.verticalLayout_8.addWidget(self.drugi_input)
        spacerItem2 = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_8.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        self.glavni_btn = QtGui.QPushButton(self.centralwidget)
        self.glavni_btn.setObjectName(_fromUtf8("glavni_btn"))
        self.verticalLayout_6.addWidget(self.glavni_btn)
        spacerItem3 = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        spacerItem4 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuTestic = QtGui.QMenu(self.menubar)
        self.menuTestic.setObjectName(_fromUtf8("menuTestic"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSdsa = QtGui.QAction(MainWindow)
        self.actionSdsa.setObjectName(_fromUtf8("actionSdsa"))
        self.actionSadas = QtGui.QAction(MainWindow)
        self.actionSadas.setObjectName(_fromUtf8("actionSadas"))
        self.actionSda = QtGui.QAction(MainWindow)
        self.actionSda.setObjectName(_fromUtf8("actionSda"))
        self.actionAsd = QtGui.QAction(MainWindow)
        self.actionAsd.setObjectName(_fromUtf8("actionAsd"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setCheckable(False)
        self.actionAbout.setWhatsThis(_fromUtf8(""))
        self.actionAbout.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionTestic = QtGui.QAction(MainWindow)
        self.actionTestic.setObjectName(_fromUtf8("actionTestic"))
        self.menuHelp.addAction(self.actionAbout)
        self.menuTestic.addAction(self.actionTestic)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuTestic.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Lesa", None))
        self.vrijeme_lbl.setText(_translate("MainWindow", "0:0:0", None))
        self.start.setText(_translate("MainWindow", "START", None))
        self.stop.setText(_translate("MainWindow", "STOP", None))
        self.reset.setText(_translate("MainWindow", "RESET", None))
        self.label_2.setText(_translate("MainWindow", "Ime", None))
        self.label.setText(_translate("MainWindow", "Prezime", None))
        self.glavni_btn.setText(_translate("MainWindow", "Save", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuTestic.setTitle(_translate("MainWindow", "Drugi", None))
        self.actionSdsa.setText(_translate("MainWindow", "sdsa", None))
        self.actionSadas.setText(_translate("MainWindow", "sadas", None))
        self.actionSda.setText(_translate("MainWindow", "sda", None))
        self.actionAsd.setText(_translate("MainWindow", "asd", None))
        self.actionAbout.setText(_translate("MainWindow", "About Lesa", None))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About dude Lesa", None))
        self.actionTestic.setText(_translate("MainWindow", "Testic", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

