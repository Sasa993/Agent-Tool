# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_top10_quickest_calls.ui'
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

class Ui_Top10QuickestCallsDialog(object):
    def setupUi(self, Top10QuickestCallsDialog):
        Top10QuickestCallsDialog.setObjectName(_fromUtf8("Top10QuickestCallsDialog"))
        Top10QuickestCallsDialog.resize(680, 486)
        Top10QuickestCallsDialog.setMinimumSize(QtCore.QSize(680, 486))
        Top10QuickestCallsDialog.setMaximumSize(QtCore.QSize(680, 486))
        self.tableWidgetTop10QuickestCalls = QtGui.QTableWidget(Top10QuickestCallsDialog)
        self.tableWidgetTop10QuickestCalls.setGeometry(QtCore.QRect(30, 50, 621, 341))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetTop10QuickestCalls.sizePolicy().hasHeightForWidth())
        self.tableWidgetTop10QuickestCalls.setSizePolicy(sizePolicy)
        self.tableWidgetTop10QuickestCalls.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidgetTop10QuickestCalls.setMaximumSize(QtCore.QSize(621, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tableWidgetTop10QuickestCalls.setFont(font)
        self.tableWidgetTop10QuickestCalls.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidgetTop10QuickestCalls.setLineWidth(1)
        self.tableWidgetTop10QuickestCalls.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetTop10QuickestCalls.setAutoScrollMargin(16)
        self.tableWidgetTop10QuickestCalls.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetTop10QuickestCalls.setAlternatingRowColors(True)
        self.tableWidgetTop10QuickestCalls.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetTop10QuickestCalls.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetTop10QuickestCalls.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidgetTop10QuickestCalls.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.tableWidgetTop10QuickestCalls.setShowGrid(False)
        self.tableWidgetTop10QuickestCalls.setWordWrap(True)
        self.tableWidgetTop10QuickestCalls.setObjectName(_fromUtf8("tableWidgetTop10QuickestCalls"))
        self.tableWidgetTop10QuickestCalls.setColumnCount(6)
        self.tableWidgetTop10QuickestCalls.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10QuickestCalls.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10QuickestCalls.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10QuickestCalls.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10QuickestCalls.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10QuickestCalls.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetTop10QuickestCalls.setHorizontalHeaderItem(5, item)
        self.tableWidgetTop10QuickestCalls.horizontalHeader().setVisible(True)
        self.tableWidgetTop10QuickestCalls.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetTop10QuickestCalls.horizontalHeader().setDefaultSectionSize(103)
        self.tableWidgetTop10QuickestCalls.horizontalHeader().setHighlightSections(False)
        self.tableWidgetTop10QuickestCalls.horizontalHeader().setMinimumSectionSize(33)
        self.tableWidgetTop10QuickestCalls.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetTop10QuickestCalls.verticalHeader().setVisible(False)
        self.tableWidgetTop10QuickestCalls.verticalHeader().setDefaultSectionSize(30)
        self.tableWidgetTop10QuickestCalls.verticalHeader().setHighlightSections(False)
        self.pushButtonSelektovano = QtGui.QPushButton(Top10QuickestCallsDialog)
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
        self.label = QtGui.QLabel(Top10QuickestCallsDialog)
        self.label.setGeometry(QtCore.QRect(240, 12, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Top10QuickestCallsDialog)
        QtCore.QMetaObject.connectSlotsByName(Top10QuickestCallsDialog)

    def retranslateUi(self, Top10QuickestCallsDialog):
        Top10QuickestCallsDialog.setWindowTitle(_translate("Top10QuickestCallsDialog", "Dialog", None))
        self.tableWidgetTop10QuickestCalls.setSortingEnabled(True)
        item = self.tableWidgetTop10QuickestCalls.horizontalHeaderItem(0)
        item.setText(_translate("Top10QuickestCallsDialog", "ID", None))
        item = self.tableWidgetTop10QuickestCalls.horizontalHeaderItem(1)
        item.setText(_translate("Top10QuickestCallsDialog", "Ticket number", None))
        item = self.tableWidgetTop10QuickestCalls.horizontalHeaderItem(2)
        item.setText(_translate("Top10QuickestCallsDialog", "Severity", None))
        item = self.tableWidgetTop10QuickestCalls.horizontalHeaderItem(3)
        item.setText(_translate("Top10QuickestCallsDialog", "Status", None))
        item = self.tableWidgetTop10QuickestCalls.horizontalHeaderItem(4)
        item.setText(_translate("Top10QuickestCallsDialog", "Date", None))
        item = self.tableWidgetTop10QuickestCalls.horizontalHeaderItem(5)
        item.setText(_translate("Top10QuickestCallsDialog", "Duration", None))
        self.pushButtonSelektovano.setText(_translate("Top10QuickestCallsDialog", " SELECT", None))
        self.label.setText(_translate("Top10QuickestCallsDialog", "TOP 10 QUICKEST CALLS", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Top10QuickestCallsDialog = QtGui.QDialog()
    ui = Ui_Top10QuickestCallsDialog()
    ui.setupUi(Top10QuickestCallsDialog)
    Top10QuickestCallsDialog.show()
    sys.exit(app.exec_())

