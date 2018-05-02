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
		self.ispis_iz_baze()

	def ispis_iz_baze(self):
		conn = sqlite3.connect("baza.db")
		c = conn.cursor()

		rezultat = c.execute("SELECT * FROM test1")

		for x in rezultat:
			self.label_ispis.addItem("{0}. {1} {2}".format(str(x[0]), x[1], x[2]))
			# print(x)

		conn.commit()
		conn.close()
		
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):

		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.glavni_btn.setDisabled(True)
		self.prvi_input.textChanged.connect(self.disable_glavni_btn)
		self.prvi_input.textChanged.connect(lambda: self.prvi_input(prvi_input))
		self.drugi_input.textChanged.connect(self.disable_glavni_btn)
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

		#if (ime == "" or prezime == ""):
			#self.test_label.setText("NE MOZE!")
		#else:
			#connection.execute("INSERT INTO test1 VALUES(NULL, ?, ?)", (ime, prezime))
			#connection.commit()

		connection.execute("INSERT INTO test1 VALUES(NULL, ?, ?)", (ime, prezime))
		connection.commit()
		connection.close()

		self.prvi_input.clear()
		self.drugi_input.clear()
		self.glavni_btn.setDisabled(True)

	def disable_glavni_btn(self):
		if (len(self.prvi_input.text()) > 0 and len(self.drugi_input.text()) > 0):
			self.glavni_btn.setDisabled(False)
			
		else:
			self.glavni_btn.setDisabled(True)

	def red_prvi_input(self, koji_input):
		if (len(self.koji_input.text() < 1)):
			self.koji_input.setStyleSheet('QWidget{background-color: rgb(255, 36, 8)}')
		else:
			self.koji_input.setStyleSheet('QWidget{background-color: rgb()}')


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