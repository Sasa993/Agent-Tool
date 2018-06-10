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
        testWidget.resize(753, 652)
        testWidget.setMinimumSize(QtCore.QSize(753, 652))
        testWidget.setMaximumSize(QtCore.QSize(753, 652))
        self.layoutWidget = QtGui.QWidget(testWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(197, 70, 551, 501))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(5, -1, 5, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.layoutWidget)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 541, 499))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetIspisIzBaze = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetIspisIzBaze.sizePolicy().hasHeightForWidth())
        self.tableWidgetIspisIzBaze.setSizePolicy(sizePolicy)
        self.tableWidgetIspisIzBaze.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidgetIspisIzBaze.setMaximumSize(QtCore.QSize(517, 16777215))
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
        self.tableWidgetIspisIzBaze.setLineWidth(1)
        self.tableWidgetIspisIzBaze.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetIspisIzBaze.setAutoScrollMargin(16)
        self.tableWidgetIspisIzBaze.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetIspisIzBaze.setAlternatingRowColors(True)
        self.tableWidgetIspisIzBaze.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidgetIspisIzBaze.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidgetIspisIzBaze.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidgetIspisIzBaze.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
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
        self.tableWidgetIspisIzBaze.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetIspisIzBaze.horizontalHeader().setDefaultSectionSize(103)
        self.tableWidgetIspisIzBaze.horizontalHeader().setHighlightSections(False)
        self.tableWidgetIspisIzBaze.horizontalHeader().setMinimumSectionSize(33)
        self.tableWidgetIspisIzBaze.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetIspisIzBaze.verticalHeader().setVisible(False)
        self.tableWidgetIspisIzBaze.verticalHeader().setDefaultSectionSize(30)
        self.tableWidgetIspisIzBaze.verticalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.tableWidgetIspisIzBaze)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtGui.QWidget(testWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(400, 9, 331, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtGui.QWidget(testWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(26, 70, 171, 490))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(-1, 60, -1, 60)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelkita = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelkita.setFont(font)
        self.labelkita.setStyleSheet(_fromUtf8("QLabel { \n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"border-top: 1px solid black;\n"
"background-color: rgb(84, 255, 155);\n"
"}"))
        self.labelkita.setAlignment(QtCore.Qt.AlignCenter)
        self.labelkita.setObjectName(_fromUtf8("labelkita"))
        self.verticalLayout_3.addWidget(self.labelkita)
        self.labelBrojTiketaDanas = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelBrojTiketaDanas.setFont(font)
        self.labelBrojTiketaDanas.setStyleSheet(_fromUtf8("QLabel {\n"
"background-color: rgb(196, 255, 218);\n"
"border-top: 1px solid black;\n"
"}\n"
"QLabel:hover {\n"
"border-top: 0;\n"
"border-right: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-bottom: 1px solid black\n"
"}"))
        self.labelBrojTiketaDanas.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBrojTiketaDanas.setObjectName(_fromUtf8("labelBrojTiketaDanas"))
        self.verticalLayout_3.addWidget(self.labelBrojTiketaDanas)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("QLabel { \n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"border-top: 1px solid black;\n"
"background-color: rgb(84, 255, 155);\n"
"}"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.labelBrojTiketaMjesec = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelBrojTiketaMjesec.setFont(font)
        self.labelBrojTiketaMjesec.setStyleSheet(_fromUtf8("QLabel {\n"
"background-color: rgb(196, 255, 218);\n"
"border-top: 1px solid black;\n"
"}\n"
"QLabel:hover {\n"
"border-top: 0;\n"
"border-right: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-bottom: 1px solid black\n"
"}"))
        self.labelBrojTiketaMjesec.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBrojTiketaMjesec.setObjectName(_fromUtf8("labelBrojTiketaMjesec"))
        self.verticalLayout_3.addWidget(self.labelBrojTiketaMjesec)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("QLabel { \n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;\n"
"border-top: 1px solid black;\n"
"background-color: rgb(84, 255, 155);\n"
"}"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.labelSrednjaVrijednostDuzine = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelSrednjaVrijednostDuzine.setFont(font)
        self.labelSrednjaVrijednostDuzine.setStyleSheet(_fromUtf8("QLabel {\n"
"background-color: rgb(196, 255, 218);\n"
"border-top: 1px solid black;\n"
"}\n"
"QLabel:hover {\n"
"border-top: 0;\n"
"border-right: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-bottom: 1px solid black\n"
"}"))
        self.labelSrednjaVrijednostDuzine.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSrednjaVrijednostDuzine.setObjectName(_fromUtf8("labelSrednjaVrijednostDuzine"))
        self.verticalLayout_3.addWidget(self.labelSrednjaVrijednostDuzine)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(testWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(216, 580, 511, 61))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 10)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonSelektovano = QtGui.QPushButton(self.horizontalLayoutWidget_2)
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
        self.horizontalLayout_2.addWidget(self.pushButtonSelektovano)
        self.pushButtonRefresh = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRefresh.sizePolicy().hasHeightForWidth())
        self.pushButtonRefresh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonRefresh.setFont(font)
        self.pushButtonRefresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonRefresh.setStyleSheet(_fromUtf8("QPushButton:hover {background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.988636, y2:0.983, stop:0 rgba(96, 255, 170, 255), stop:0.664773 rgba(255, 255, 255, 255));}\n"
"QPushButton:pressed { border: 1px solid black;}\n"
"QPushButton { background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(96, 255, 170, 255), stop:0.664773 rgba(255, 255, 255, 255)); border-radius: 20px; }\n"
"\n"
""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/001-circular-arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRefresh.setIcon(icon1)
        self.pushButtonRefresh.setIconSize(QtCore.QSize(32, 32))
        self.pushButtonRefresh.setObjectName(_fromUtf8("pushButtonRefresh"))
        self.horizontalLayout_2.addWidget(self.pushButtonRefresh)

        self.retranslateUi(testWidget)
        QtCore.QMetaObject.connectSlotsByName(testWidget)

    def retranslateUi(self, testWidget):
        testWidget.setWindowTitle(_translate("testWidget", "Tickets", None))
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
        self.pushButton.setText(_translate("testWidget", "Search", None))
        self.labelkita.setText(_translate("testWidget", "Today", None))
        self.labelBrojTiketaDanas.setText(_translate("testWidget", "a", None))
        self.label_3.setText(_translate("testWidget", "This month", None))
        self.labelBrojTiketaMjesec.setText(_translate("testWidget", "a", None))
        self.label_2.setText(_translate("testWidget", "Avarage handling time", None))
        self.labelSrednjaVrijednostDuzine.setText(_translate("testWidget", "a", None))
        self.pushButtonSelektovano.setText(_translate("testWidget", " SELECT", None))
        self.pushButtonRefresh.setText(_translate("testWidget", " REFRESH", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    testWidget = QtGui.QWidget()
    ui = Ui_testWidget()
    ui.setupUi(testWidget)
    testWidget.show()
    sys.exit(app.exec_())

