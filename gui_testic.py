# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_testic.ui'
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

class Ui_testWidget(object):
    def setupUi(self, testWidget):
        testWidget.setObjectName(_fromUtf8("testWidget"))
        testWidget.setWindowModality(QtCore.Qt.NonModal)
        testWidget.resize(850, 634)
        testWidget.setMaximumSize(QtCore.QSize(850, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(testWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(testWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 828, 612))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.toolBox = QtGui.QToolBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 810, 559))
        self.page.setObjectName(_fromUtf8("page"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.page)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 110, 361, 251))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        # self.toolBox.addItem(self.page, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.toolBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(testWidget)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(8)
        QtCore.QMetaObject.connectSlotsByName(testWidget)

    def retranslateUi(self, testWidget):
        testWidget.setWindowTitle(_translate("testWidget", "Form", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("testWidget", "Page 1", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    testWidget = QtGui.QWidget()
    ui = Ui_testWidget()
    ui.setupUi(testWidget)
    testWidget.show()
    sys.exit(app.exec_())

