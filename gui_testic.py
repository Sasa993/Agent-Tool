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
        testWidget.resize(342, 295)
        self.label = QtGui.QLabel(testWidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(17, 140, 255);"))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(testWidget)
        QtCore.QMetaObject.connectSlotsByName(testWidget)

    def retranslateUi(self, testWidget):
        testWidget.setWindowTitle(_translate("testWidget", "Form", None))
        self.label.setText(_translate("testWidget", "Kurac palac", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    testWidget = QtGui.QWidget()
    ui = Ui_testWidget()
    ui.setupUi(testWidget)
    testWidget.show()
    sys.exit(app.exec_())

