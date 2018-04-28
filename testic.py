import sys
import sqlite3
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "gui_fajl.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.button.clicked.connect(self.click_on_button)

	def click_on_button(self):
		connection = sqlite3.connect("baza.db")

		ime = str(self.prvi_input.text())
		prezime = str(self.drugi_input.text())

		connection.execute("INSERT INTO users3 VALUES(NULL, ?, ?)", (ime, prezime))
		connection.commit()
		connection.close()

		self.prvi_input.clear()
		self.drugi_input.clear()

	def click_on_button_exit(self):
		sys.exit()

	def closeEvent(self, event):
	    pitanje = "Are you sure you want to exit the program?"
	    reply = QtGui.QMessageBox.question(self, 'Message', 
	                     pitanje, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

	    if reply == QtGui.QMessageBox.Yes:
	        event.accept()
	    else:
	        event.ignore()

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())