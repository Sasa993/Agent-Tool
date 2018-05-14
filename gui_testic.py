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
        testWidget.resize(562, 634)
        testWidget.setMinimumSize(QtCore.QSize(0, 0))
        testWidget.setMaximumSize(QtCore.QSize(562, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(testWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(10, -1, 10, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(testWidget)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 524, 614))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButtonRefresh = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonRefresh.setObjectName(_fromUtf8("pushButtonRefresh"))
        self.verticalLayout_2.addWidget(self.pushButtonRefresh)
        self.tableWidgetIspisIzBaze = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetIspisIzBaze.sizePolicy().hasHeightForWidth())
        self.tableWidgetIspisIzBaze.setSizePolicy(sizePolicy)
        self.tableWidgetIspisIzBaze.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidgetIspisIzBaze.setMaximumSize(QtCore.QSize(502, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tableWidgetIspisIzBaze.setFont(font)
        self.tableWidgetIspisIzBaze.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidgetIspisIzBaze.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetIspisIzBaze.setAlternatingRowColors(True)
        self.tableWidgetIspisIzBaze.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetIspisIzBaze.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetIspisIzBaze.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidgetIspisIzBaze.setShowGrid(False)
        self.tableWidgetIspisIzBaze.setWordWrap(True)
        self.tableWidgetIspisIzBaze.setObjectName(_fromUtf8("tableWidgetIspisIzBaze"))
        self.tableWidgetIspisIzBaze.setColumnCount(5)
        self.tableWidgetIspisIzBaze.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetIspisIzBaze.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetIspisIzBaze.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetIspisIzBaze.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetIspisIzBaze.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetIspisIzBaze.setHorizontalHeaderItem(4, item)
        self.tableWidgetIspisIzBaze.horizontalHeader().setVisible(True)
        self.tableWidgetIspisIzBaze.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidgetIspisIzBaze.horizontalHeader().setHighlightSections(False)
        self.tableWidgetIspisIzBaze.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetIspisIzBaze.verticalHeader().setVisible(False)
        self.tableWidgetIspisIzBaze.verticalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.tableWidgetIspisIzBaze)
        self.pushButtonSelektovano = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonSelektovano.setObjectName(_fromUtf8("pushButtonSelektovano"))
        self.verticalLayout_2.addWidget(self.pushButtonSelektovano)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(testWidget)
        QtCore.QMetaObject.connectSlotsByName(testWidget)

    def retranslateUi(self, testWidget):
        testWidget.setWindowTitle(_translate("testWidget", "Form", None))
        self.pushButtonRefresh.setText(_translate("testWidget", "REFRESH", None))
        self.tableWidgetIspisIzBaze.setSortingEnabled(True)
        item = self.tableWidgetIspisIzBaze.horizontalHeaderItem(0)
        item.setText(_translate("testWidget", "ID", None))
        item = self.tableWidgetIspisIzBaze.horizontalHeaderItem(1)
        item.setText(_translate("testWidget", "Ticket number", None))
        item = self.tableWidgetIspisIzBaze.horizontalHeaderItem(2)
        item.setText(_translate("testWidget", "Severity", None))
        item = self.tableWidgetIspisIzBaze.horizontalHeaderItem(3)
        item.setText(_translate("testWidget", "Status", None))
        item = self.tableWidgetIspisIzBaze.horizontalHeaderItem(4)
        item.setText(_translate("testWidget", "Date", None))
        self.pushButtonSelektovano.setText(_translate("testWidget", "SELECT", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    testWidget = QtGui.QWidget()
    ui = Ui_testWidget()
    ui.setupUi(testWidget)
    testWidget.show()
    sys.exit(app.exec_())

