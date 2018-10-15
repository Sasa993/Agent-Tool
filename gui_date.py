# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_date.ui'
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

class Ui_DateDialog(object):
    def setupUi(self, DateDialog):
        DateDialog.setObjectName(_fromUtf8("DateDialog"))
        DateDialog.resize(400, 268)
        self.pushButtonContinueDate = QtGui.QPushButton(DateDialog)
        self.pushButtonContinueDate.setGeometry(QtCore.QRect(140, 180, 111, 41))
        self.pushButtonContinueDate.setObjectName(_fromUtf8("pushButtonContinueDate"))
        self.label = QtGui.QLabel(DateDialog)
        self.label.setGeometry(QtCore.QRect(120, 70, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.dateEditDate = QtGui.QDateEdit(DateDialog)
        self.dateEditDate.setGeometry(QtCore.QRect(140, 110, 110, 22))
        self.dateEditDate.setCalendarPopup(True)
        self.dateEditDate.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEditDate.setObjectName(_fromUtf8("dateEditDate"))

        self.retranslateUi(DateDialog)
        QtCore.QMetaObject.connectSlotsByName(DateDialog)

    def retranslateUi(self, DateDialog):
        DateDialog.setWindowTitle(_translate("DateDialog", "Dialog", None))
        self.pushButtonContinueDate.setText(_translate("DateDialog", "Continue", None))
        self.label.setText(_translate("DateDialog", "Chose month and year", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DateDialog = QtGui.QDialog()
    ui = Ui_DateDialog()
    ui.setupUi(DateDialog)
    DateDialog.show()
    sys.exit(app.exec_())

