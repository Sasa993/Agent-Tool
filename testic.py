import sys
import sqlite3
from PyQt4 import QtCore, QtGui, uic
from gui_glavni import Ui_MainWindow
from gui_about import Ui_aboutDialog
from gui_testic import Ui_testWidget
import datetime

s = 0
m = 0
h = 0
provjera_button_start = True

class aboutDialog(QtGui.QDialog, Ui_aboutDialog):
	def __init__(self, parent = None):
		QtGui.QDialog.__init__(self, parent)
		flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setupUi(self)
		self.about_btn.clicked.connect(self.click_on_about_btn)

	def click_on_about_btn(self):
		self.close()

# widget za ispis iz baze
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
		
		# self.glavni_btn.setDisabled(True)
		# self.prvi_input.textChanged.connect(self.enable_glavni_btn)
		# self.drugi_input.textChanged.connect(self.enable_glavni_btn)
		# self.promjena_boje_inputa()
		
		# self.glavni_btn.clicked.connect(self.click_on_button)

		self.actionAbout.triggered.connect(self.actionAbout_triggered)
		self.popAboutDialog = aboutDialog()

		self.actionTestic.triggered.connect(self.startUi_testWidget)
		#-------------------------------------------------------------- 
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.Time)
		self.pushButton_start.clicked.connect(self.Start)
		# self.stop.clicked.connect(lambda: self.timer.stop())
		self.pushButton_reset.clicked.connect(self.Reset)

	def Reset(self):
		global s, m, h, provjera_button_start

		self.timer.stop()
		vrijeme = "{0}:{1}:{2}".format(h,m,s)
		print("Vrijeme koliko ti je trebalo da napises jebeni TIKET iznosi:\n{0}".format(vrijeme))
		provjera_button_start = True
		self.pushButton_start.setChecked(False)

		s = 0
		m = 0
		h = 0
 
		time = "{0}:{1}:{2}".format(h,m,s)
 
		# self.lcd.setDigitCount(len(time))
		# self.lcd.display(time)

		self.label_timer.setText(time)

	def Start(self):
		global s, m, h, provjera_button_start

		if (provjera_button_start == True):
			self.timer.start(1000)
			provjera_button_start = not provjera_button_start
			self.pushButton_start.setText('PAUSE')
		elif (provjera_button_start == False):
			self.timer.stop()
			provjera_button_start = not provjera_button_start
			self.pushButton_start.setText('START')

	def Time(self):
		global s,m,h

		if (s < 59):
			s += 1
		else:
			if (m < 59):
				s = 0
				m += 1
			elif (m == 59 and h < 24):
				h += 1
				m = 0
				s = 0
			else:
				self.timer.stop()

		time = "{0}:{1}:{2}".format(h, m, s)

		# self.lcd.setDigitCount(len(time))
		# self.lcd.display(time)

		self.label_timer.setText(time)

		#mjerenje vremena (mozda bi mogla biti smjena)
		# self.count = 15
		# self.interval = 1200
		# self.timer = QtCore.QTimer()
		# self.timer.timeout.connect(self.countdown)
		# self.timer.start(1000)

	# def countdown(self):
	# 	global count
	# 	if (self.count < 1):
	# 		self.count = 15
	# 	self.now = datetime.datetime.now()
	# 	self.test_label.setText('Time now: %s. End time: %s. Seconds left: %s'%(self.now.strftime("%H:%M:%S"), (self.now + datetime.timedelta(seconds=self.count)).strftime("%H:%M:%S"), self.count))
	# 	self.count = self.count - 1

	def startUi_testWidget(self):
		self.poptestWidget = Ui_testWidget()
		self.setWindowTitle("UIToolTab")
		self.setCentralWidget(self.poptestWidget)
		self.poptestWidget.show()

	# built-in event kada se ide na X da se close-a window
	# def closeEvent(self, event):
	#     pitanje = "Are you sure you want to exit the program?"
	#     reply = QtGui.QMessageBox.question(self, 'Message', 
	#                      pitanje, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

	#     if reply == QtGui.QMessageBox.Yes:
	#         event.accept()
	#     else:
	#         event.ignore()

	def actionAbout_triggered(self):
		self.popAboutDialog.show()

	# unos u bazu
	def click_on_button(self):
		connection = sqlite3.connect("baza.db")

		ime = str(self.prvi_input.text())
		prezime = str(self.drugi_input.text())

		connection.execute("INSERT INTO test1 VALUES(NULL, ?, ?)", (ime, prezime))
		connection.commit()
		connection.close()

		self.prvi_input.clear()
		self.prvi_input.setStyleSheet("QWidget { background-color: rgb(255, 255, 255)}")
		self.drugi_input.clear()
		self.drugi_input.setStyleSheet("QWidget { background-color: rgb(255, 255, 255)}")

		self.glavni_btn.setDisabled(True)	

	# vracanje glavnog_btn na "clickable" kad su inputi popunjeni
	def enable_glavni_btn(self):
		if (len(self.prvi_input.text()) > 0 and len(self.drugi_input.text()) > 0):
			self.glavni_btn.setDisabled(False)
			
		else:
			self.glavni_btn.setDisabled(True)

	# input-i koji su required, postaju odredjene boje da USER zna da je taj input required
	def promjena_boje_inputa(self):
		self.prvi_input.textChanged.connect(lambda boja: self.prvi_input.setStyleSheet(
		"QWidget { background-color: %s}" % ('rgb(255, 255, 255)' if boja else 'rgb(212, 60, 60)')))
		self.drugi_input.textChanged.connect(lambda boja: self.drugi_input.setStyleSheet(
		"QWidget { background-color: %s}" % ('rgb(255, 255, 255)' if boja else 'rgb(212, 60, 60)')))
		#ostali inputi idu ovdje

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())