# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_top10_longest_calls.ui'
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

class Ui_Top10LongestCallsDialog(object):
    def setupUi(self, Top10LongestCallsDialog):
        Top10LongestCallsDialog.setObjectName(_fromUtf8("Top10LongestCallsDialog"))
        Top10LongestCallsDialog.resize(680, 486)
        Top10LongestCallsDialog.setMinimumSize(QtCore.QSize(680, 486))
        Top10LongestCallsDialog.setMaximumSize(QtCore.QSize(680, 486))
        self.tableWidgetTop10LongestCalls = QtGui.QTableWidget(Top10LongestCallsDialog)
        self.tableWidgetTop10LongestCalls.setGeometry(QtCore.QRect(30, 50, 621, 341))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetTop10LongestCalls.sizePolicy().hasHeightForWidth())
        self.tableWidgetTop10LongestCalls.setSizePolicy(sizePolicy)
        self.tableWidgetTop10LongestCalls.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidgetTop10LongestCalls.setMaximumSize(QtCore.QSize(621, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tableWidgetTop10LongestCalls.setFont(font)
        self.tableWidgetTop10LongestCalls.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidgetTop10LongestCalls.setLineWidth(1)
        self.tableWidgetTop10LongestCalls.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetTop10LongestCalls.setAutoScrollMargin(16)
        self.tableWidgetTop10LongestCalls.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetTop10LongestCalls.setAlternatingRowColors(True)
        self.tableWidgetTop10LongestCalls.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetTop10LongestCalls.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetTop10LongestCalls.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidgetTop10LongestCalls.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.tableWidgetTop10LongestCalls.setShowGrid(False)
        self.tableWidgetTop10LongestCalls.setWordWrap(True)
        self.tableWidgetTop10LongestCalls.setObjectName(_fromUtf8("tableWidgetTop10LongestCalls"))
        self.tableWidgetTop10LongestCalls.setColumnCount(6)
        self.tableWidgetTop10LongestCalls.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10LongestCalls.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10LongestCalls.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10LongestCalls.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10LongestCalls.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10LongestCalls.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10LongestCalls.setHorizontalHeaderItem(5, item)
        self.tableWidgetTop10LongestCalls.horizontalHeader().setVisible(True)
        self.tableWidgetTop10LongestCalls.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetTop10LongestCalls.horizontalHeader().setDefaultSectionSize(103)
        self.tableWidgetTop10LongestCalls.horizontalHeader().setHighlightSections(False)
        self.tableWidgetTop10LongestCalls.horizontalHeader().setMinimumSectionSize(33)
        self.tableWidgetTop10LongestCalls.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetTop10LongestCalls.verticalHeader().setVisible(False)
        self.tableWidgetTop10LongestCalls.verticalHeader().setDefaultSectionSize(30)
        self.tableWidgetTop10LongestCalls.verticalHeader().setHighlightSections(False)
        self.pushButtonSelektovano = QtGui.QPushButton(Top10LongestCallsDialog)
        self.pushButtonSelektovano.setGeometry(QtCore.QRect(220, 400, 230, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSelektovano.sizePolicy().hasHeightForWidth())
        self.pushButtonSelektovano.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSelektovano.setFont(font)
        self.pushButtonSelektovano.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSelektovano.setStyleSheet(_fromUtf8("QPushButton:hover {background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.988636, y2:0.983, stop:0 rgba(96, 255, 170, 255), stop:0.664773 rgba(255, 255, 255, 255));}\n"
"QPushButton:pressed { border: 1px solid black;}\n"
"QPushButton { background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(96, 255, 170, 255), stop:0.664773 rgba(255, 255, 255, 255)); border-radius: 20px; }\n"
"\n"
""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/005-select.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSelektovano.setIcon(icon)
        self.pushButtonSelektovano.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonSelektovano.setObjectName(_fromUtf8("pushButtonSelektovano"))
        self.label = QtGui.QLabel(Top10LongestCallsDialog)
        self.label.setGeometry(QtCore.QRect(240, 12, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Top10LongestCallsDialog)
        QtCore.QMetaObject.connectSlotsByName(Top10LongestCallsDialog)

    def retranslateUi(self, Top10LongestCallsDialog):
        Top10LongestCallsDialog.setWindowTitle(_translate("Top10LongestCallsDialog", "Dialog", None))
        self.tableWidgetTop10LongestCalls.setSortingEnabled(True)
        item = self.tableWidgetTop10LongestCalls.horizontalHeaderItem(0)
        item.setText(_translate("Top10LongestCallsDialog", "ID", None))
        item = self.tableWidgetTop10LongestCalls.horizontalHeaderItem(1)
        item.setText(_translate("Top10LongestCallsDialog", "Ticket number", None))
        item = self.tableWidgetTop10LongestCalls.horizontalHeaderItem(2)
        item.setText(_translate("Top10LongestCallsDialog", "Severity", None))
        item = self.tableWidgetTop10LongestCalls.horizontalHeaderItem(3)
        item.setText(_translate("Top10LongestCallsDialog", "Status", None))
        item = self.tableWidgetTop10LongestCalls.horizontalHeaderItem(4)
        item.setText(_translate("Top10LongestCallsDialog", "Date", None))
        item = self.tableWidgetTop10LongestCalls.horizontalHeaderItem(5)
        item.setText(_translate("Top10LongestCallsDialog", "Duration", None))
        self.pushButtonSelektovano.setText(_translate("Top10LongestCallsDialog", " SELECT", None))
        self.label.setText(_translate("Top10LongestCallsDialog", "TOP 10 LONGEST CALLS", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Top10LongestCallsDialog = QtGui.QDialog()
    ui = Ui_Top10LongestCallsDialog()
    ui.setupUi(Top10LongestCallsDialog)
    Top10LongestCallsDialog.show()
    sys.exit(app.exec_())

