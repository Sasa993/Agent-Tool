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
		connection = sqlite3.connect("nova_baza.db")

		ime = str(self.prvi_input.text())
		ime = ime[0].upper() + ime[1:]
		prezime = str(self.drugi_input.text())

		connection.execute("INSERT INTO users VALUES(?,?)", (ime, prezime))
		connection.commit()
		connection.close()

	def ispis_iz_baze():
		connection = sqlite3.connect("baza.db")

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())