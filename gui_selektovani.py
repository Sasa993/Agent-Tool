# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_selektovani.ui'
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

class Ui_selektovaniId(object):
    def setupUi(self, selektovaniId):
        selektovaniId.setObjectName(_fromUtf8("selektovaniId"))
        selektovaniId.resize(600, 615)
        selektovaniId.setMinimumSize(QtCore.QSize(600, 563))
        selektovaniId.setMaximumSize(QtCore.QSize(1080, 700))
        selektovaniId.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.gridLayout_3 = QtGui.QGridLayout(selektovaniId)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.labelStatus = QtGui.QLabel(selektovaniId)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStatus.sizePolicy().hasHeightForWidth())
        self.labelStatus.setSizePolicy(sizePolicy)
        self.labelStatus.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelStatus.setFont(font)
        self.labelStatus.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0.0170455, x2:1, y2:0, stop:0 rgba(99, 153, 117, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.labelStatus.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.verticalLayout_6.addWidget(self.labelStatus)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 4, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelVrijeme = QtGui.QLabel(selektovaniId)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelVrijeme.setFont(font)
        self.labelVrijeme.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labelVrijeme.setObjectName(_fromUtf8("labelVrijeme"))
        self.horizontalLayout_3.addWidget(self.labelVrijeme)
        self.labelIncidentNumber = QtGui.QLabel(selektovaniId)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelIncidentNumber.setFont(font)
        self.labelIncidentNumber.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelIncidentNumber.setObjectName(_fromUtf8("labelIncidentNumber"))
        self.horizontalLayout_3.addWidget(self.labelIncidentNumber)
        self.labelSeverity = QtGui.QLabel(selektovaniId)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSeverity.setFont(font)
        self.labelSeverity.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.labelSeverity.setObjectName(_fromUtf8("labelSeverity"))
        self.horizontalLayout_3.addWidget(self.labelSeverity)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.line_23 = QtGui.QFrame(selektovaniId)
        self.line_23.setStyleSheet(_fromUtf8("color: rgb(129, 255, 148);"))
        self.line_23.setFrameShape(QtGui.QFrame.HLine)
        self.line_23.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_23.setObjectName(_fromUtf8("line_23"))
        self.gridLayout_3.addWidget(self.line_23, 1, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plainTextEditOutput = QtGui.QPlainTextEdit(selektovaniId)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.plainTextEditOutput.setFont(font)
        self.plainTextEditOutput.setMouseTracking(False)
        self.plainTextEditOutput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEditOutput.setAutoFillBackground(False)
        self.plainTextEditOutput.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.plainTextEditOutput.setFrameShape(QtGui.QFrame.WinPanel)
        self.plainTextEditOutput.setFrameShadow(QtGui.QFrame.Raised)
        self.plainTextEditOutput.setLineWidth(1)
        self.plainTextEditOutput.setMidLineWidth(1)
        self.plainTextEditOutput.setTabChangesFocus(True)
        self.plainTextEditOutput.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEditOutput.setObjectName(_fromUtf8("plainTextEditOutput"))
        self.gridLayout.addWidget(self.plainTextEditOutput, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 2)

        self.retranslateUi(selektovaniId)
        QtCore.QMetaObject.connectSlotsByName(selektovaniId)

    def retranslateUi(self, selektovaniId):
        selektovaniId.setWindowTitle(_translate("selektovaniId", "Form", None))
        self.labelStatus.setText(_translate("selektovaniId", "Closed", None))
        self.labelVrijeme.setText(_translate("selektovaniId", "TextLabel", None))
        self.labelIncidentNumber.setText(_translate("selektovaniId", "TextLabel", None))
        self.labelSeverity.setText(_translate("selektovaniId", "TextLabel", None))
        self.plainTextEditOutput.setPlainText(_translate("selektovaniId", "asd\n"
"Site/Tree/Key #: das\n"
"Date / Time issue occurs: 05/22/2018\n"
"\n"
"Point of Contact (First and Last name): as\n"
"Site/Point of Contact Phone#: das\n"
"Site/Point of Contact Email: da\n"
"\n"
"Description of the Probblem:\n"
"sdasd\n"
"\n"
"Has site ever called support for the same issue?: asd\n"
"\n"
"Did it ever work?: N/A\n"
"\n"
"When did it stop working: N/A\n"
"Changes made around that time: N/A\n"
"\n"
"How many terminals on location: N/A\n"
"How many terminals are down: N/A\n"
"Are any of the affected terminals specialty terminals?: N/A\n"
"\n"
"Reproduction and Troubleshooting steps taken to resolve:\n"
"\n"
"asd\n"
"\n"
"Screen shots attached (if applicable): N/A\n"
"Model & S/N (if hardware related): N/A\n"
"Alternative method that will be used by the site: N/A\n"
"\n"
"***Next Steps for next contact:\n"
"N/A", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    selektovaniId = QtGui.QWidget()
    ui = Ui_selektovaniId()
    ui.setupUi(selektovaniId)
    selektovaniId.show()
    sys.exit(app.exec_())

