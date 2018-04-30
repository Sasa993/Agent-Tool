import sys
import sqlite3
from PyQt4 import QtCore, QtGui, uic
from gui_fajl import Ui_MainWindow
from gui_about import Ui_aboutDialog
from gui_testic import Ui_testWidget

class aboutDialog(QtGui.QDialog, Ui_aboutDialog):
	def __init__(self, parent = None):
		QtGui.QDialog.__init__(self, parent)
		flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setupUi(self)
		self.about_btn.clicked.connect(self.click_on_about_btn)

	def click_on_about_btn(self):
		self.close()

class Ui_testWidget(QtGui.QWidget, Ui_testWidget):
	def __init__(self, parent = None):
		# super(Ui_testWidget, self).__init__(parent)
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.glavni_btn.clicked.connect(self.click_on_button)

		self.actionAbout.triggered.connect(self.actionAbout_triggered)
		self.popAboutDialog = aboutDialog()

		self.actionTestic.triggered.connect(self.startUi_testWidget)
		

	def startUi_testWidget(self):
		self.poptestWidget = Ui_testWidget()
		self.setWindowTitle("UIToolTab")
		self.setCentralWidget(self.poptestWidget)
		self.poptestWidget.show()

	def click_on_button(self):
		connection = sqlite3.connect("baza.db")

		ime = str(self.prvi_input.text())
		prezime = str(self.drugi_input.text())

		connection.execute("INSERT INTO test1 VALUES(NULL, ?, ?)", (ime, prezime))
		connection.commit()
		connection.close()

		self.prvi_input.clear()
		self.drugi_input.clear()

	def closeEvent(self, event):
	    pitanje = "Are you sure you want to exit the program?"
	    reply = QtGui.QMessageBox.question(self, 'Message', 
	                     pitanje, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

	    if reply == QtGui.QMessageBox.Yes:
	        event.accept()
	    else:
	        event.ignore()

	def actionAbout_triggered(self):
		self.popAboutDialog.show()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())