# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_month.ui'
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

class Ui_MonthDialog(object):
    def setupUi(self, MonthDialog):
        MonthDialog.setObjectName(_fromUtf8("MonthDialog"))
        MonthDialog.resize(400, 300)
        self.label = QtGui.QLabel(MonthDialog)
        self.label.setGeometry(QtCore.QRect(120, 80, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButtonContinueMonth = QtGui.QPushButton(MonthDialog)
        self.pushButtonContinueMonth.setGeometry(QtCore.QRect(140, 200, 111, 41))
        self.pushButtonContinueMonth.setObjectName(_fromUtf8("pushButtonContinueMonth"))
        self.dateEditMonth = QtGui.QDateEdit(MonthDialog)
        self.dateEditMonth.setGeometry(QtCore.QRect(140, 110, 110, 22))
        self.dateEditMonth.setWrapping(False)
        self.dateEditMonth.setFrame(True)
        self.dateEditMonth.setAccelerated(False)
        self.dateEditMonth.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.dateEditMonth.setKeyboardTracking(True)
        self.dateEditMonth.setProperty("showGroupSeparator", False)
        self.dateEditMonth.setMinimumDate(QtCore.QDate(2018, 1, 1))
        self.dateEditMonth.setCurrentSection(QtGui.QDateTimeEdit.MonthSection)
        self.dateEditMonth.setCalendarPopup(False)
        self.dateEditMonth.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEditMonth.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEditMonth.setObjectName(_fromUtf8("dateEditMonth"))

        self.retranslateUi(MonthDialog)
        QtCore.QMetaObject.connectSlotsByName(MonthDialog)

    def retranslateUi(self, MonthDialog):
        MonthDialog.setWindowTitle(_translate("MonthDialog", "Dialog", None))
        self.label.setText(_translate("MonthDialog", "Chose month and year", None))
        self.pushButtonContinueMonth.setText(_translate("MonthDialog", "Continue", None))
        self.dateEditMonth.setDisplayFormat(_translate("MonthDialog", "M/yyyy", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MonthDialog = QtGui.QDialog()
    ui = Ui_MonthDialog()
    ui.setupUi(MonthDialog)
    MonthDialog.show()
    sys.exit(app.exec_())

