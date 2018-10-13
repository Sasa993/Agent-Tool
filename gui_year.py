# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_year.ui'
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

class Ui_YearDialog(object):
    def setupUi(self, YearDialog):
        YearDialog.setObjectName(_fromUtf8("YearDialog"))
        YearDialog.resize(400, 300)
        self.dateEditYear = QtGui.QDateEdit(YearDialog)
        self.dateEditYear.setGeometry(QtCore.QRect(140, 130, 110, 22))
        self.dateEditYear.setWrapping(False)
        self.dateEditYear.setFrame(True)
        self.dateEditYear.setKeyboardTracking(True)
        self.dateEditYear.setProperty("showGroupSeparator", False)
        self.dateEditYear.setMinimumDate(QtCore.QDate(2018, 1, 1))
        self.dateEditYear.setCalendarPopup(False)
        self.dateEditYear.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEditYear.setObjectName(_fromUtf8("dateEditYear"))
        self.label = QtGui.QLabel(YearDialog)
        self.label.setGeometry(QtCore.QRect(140, 100, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButtonContinueYear = QtGui.QPushButton(YearDialog)
        self.pushButtonContinueYear.setGeometry(QtCore.QRect(140, 220, 111, 41))
        self.pushButtonContinueYear.setObjectName(_fromUtf8("pushButtonContinueYear"))

        self.retranslateUi(YearDialog)
        QtCore.QMetaObject.connectSlotsByName(YearDialog)

    def retranslateUi(self, YearDialog):
        YearDialog.setWindowTitle(_translate("YearDialog", "Dialog", None))
        self.dateEditYear.setDisplayFormat(_translate("YearDialog", "yyyy", None))
        self.label.setText(_translate("YearDialog", "Chose a year", None))
        self.pushButtonContinueYear.setText(_translate("YearDialog", "Continue", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    YearDialog = QtGui.QDialog()
    ui = Ui_YearDialog()
    ui.setupUi(YearDialog)
    YearDialog.show()
    sys.exit(app.exec_())

