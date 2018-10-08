# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_charts.ui'
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

class Ui_Charts(object):
    def setupUi(self, Charts):
        Charts.setObjectName(_fromUtf8("Charts"))
        Charts.resize(530, 446)
        self.label = QtGui.QLabel(Charts)
        self.label.setGeometry(QtCore.QRect(230, 170, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Charts)
        QtCore.QMetaObject.connectSlotsByName(Charts)

    def retranslateUi(self, Charts):
        Charts.setWindowTitle(_translate("Charts", "Form", None))
        self.label.setText(_translate("Charts", "TEST", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Charts = QtGui.QWidget()
    ui = Ui_Charts()
    ui.setupUi(Charts)
    Charts.show()
    sys.exit(app.exec_())

