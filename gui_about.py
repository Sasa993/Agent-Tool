# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_about.ui'
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

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        aboutDialog.resize(321, 239)
        aboutDialog.setMinimumSize(QtCore.QSize(321, 239))
        aboutDialog.setMaximumSize(QtCore.QSize(321, 239))
        aboutDialog.setAutoFillBackground(False)
        aboutDialog.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.about_btn = QtGui.QPushButton(aboutDialog)
        self.about_btn.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.about_btn.setAutoFillBackground(False)
        self.about_btn.setStyleSheet(_fromUtf8("background-color: rgb(197, 195, 190);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);"))
        self.about_btn.setDefault(False)
        self.about_btn.setFlat(False)
        self.about_btn.setObjectName(_fromUtf8("about_btn"))
        self.label_about = QtGui.QLabel(aboutDialog)
        self.label_about.setGeometry(QtCore.QRect(20, 20, 281, 171))
        self.label_about.setAutoFillBackground(False)
        self.label_about.setTextFormat(QtCore.Qt.RichText)
        self.label_about.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_about.setWordWrap(True)
        self.label_about.setObjectName(_fromUtf8("label_about"))

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(_translate("aboutDialog", "Dialog", None))
        self.about_btn.setText(_translate("aboutDialog", "OK", None))
        self.label_about.setText(_translate("aboutDialog", "<html><head/><body><p align=\"justify\"><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-size:16pt; font-weight:600; color:#7a513d; background-color:#ffffff;\">Lorem Ipsum</span><span style=\" font-family:\'Open Sans,Arial,sans-serif\'; font-size:14px; color:#000000; background-color:#ffffff;\"> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. </span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    aboutDialog = QtGui.QDialog()
    ui = Ui_aboutDialog()
    ui.setupUi(aboutDialog)
    aboutDialog.show()
    sys.exit(app.exec_())

