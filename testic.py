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
provjeraButtonStart = True

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
		conn = sqlite3.connect("baza_main.db")
		c = conn.cursor()

		rezultat = c.execute("SELECT * FROM ticket_info")
		for x in rezultat:
			self.label_ispis.addItem("{0}. {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24}".format(str(x[0]), x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[21], x[22], x[23], x[24]))
			# print(x)

		conn.commit()
		conn.close()

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):

		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)

		# pushButtonCopyToClipboard i pushButtonSave disabling
		self.pushButtonCopyToClipboard.setDisabled(True)
		self.pushButtonSave.setDisabled(True)

		self.plainTextEditVersions.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditHasSiteEverCalled.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditDidItEverWork.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditWhenDidItStop.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditChangesMade.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditHowManyTermLocation.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditHowManyTermDown.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditAnyAffected.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditScreenshotsAttached.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditModelSerial.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditAlternativeMethod.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.plainTextEditNextSteps.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.plainTextEditDescriptionProblem.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.plainTextEditReporoductionTroubleshooting.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)

		self.pushButtonClearAllFields.clicked.connect(self.clear_all_fields)
		self.pushButtonCopyToClipboard.clicked.connect(self.click_on_pushButtonCopyToClipboard)
		self.now = str(datetime.date.today().strftime("%m/%d/%Y"))
		self.lineEditDatum.setText(self.now)
		
		self.pushButtonSave.clicked.connect(self.click_on_pushButtonSave_btn)
		# self.pushButtonSave.clicked.connect(self.clear_all_fields)

		self.actionAbout.triggered.connect(self.actionAbout_triggered)
		self.popAboutDialog = aboutDialog()

		self.actionTestic.triggered.connect(self.startUi_testWidget)

		# timer
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.timer_time)
		self.pushButtonStart.clicked.connect(self.timer_start)
		self.pushButtonReset.clicked.connect(self.timer_reset)

		# N/A
		self.pushButtonNaDidItEverWork.clicked.connect(lambda: self.dodavanje_na(self.lineEditDidItEverWork))
		self.pushButtonNaWhenDidItStop.clicked.connect(lambda: self.dodavanje_na(self.lineEditWhenDidItStop))
		self.pushButtonNaChangesMade.clicked.connect(lambda: self.dodavanje_na(self.lineEditChangesMade))
		self.pushButtonNaHowManyTermLocation.clicked.connect(lambda: self.dodavanje_na(self.lineEditHowManyTermLocation))
		self.pushButtonNaHowManyTermDown.clicked.connect(lambda: self.dodavanje_na(self.lineEditHowManyTermDown))
		self.pushButtonNaAnyAffected.clicked.connect(lambda: self.dodavanje_na(self.lineEditAnyAffected))
		self.pushButtonNaScreenshotsAttached.clicked.connect(lambda: self.dodavanje_na(self.lineEditScreenshotsAttached))
		self.pushButtonNaModelSerial.clicked.connect(lambda: self.dodavanje_na(self.lineEditModelSerial))
		self.pushButtonNaAlternativeMethod.clicked.connect(lambda: self.dodavanje_na(self.lineEditAlternativeMethod))
		self.pushButtonNaNextSteps.clicked.connect(lambda: self.plainTextEditNextSteps.setPlainText("N/A"))

	def timer_reset(self):
		global s, m, h, provjeraButtonStart

		self.timer.stop()
		provjeraButtonStart = True
		self.pushButtonStart.setChecked(False)

		s = 0
		m = 0
		h = 0
 
		time = "{0}:{1}:{2}".format(h,m,s)

		self.labelTimer.setText(time)

	def timer_start(self):
		global s, m, h, provjeraButtonStart

		if (provjeraButtonStart):
			self.timer.start(1000)
			provjeraButtonStart = not provjeraButtonStart
			self.pushButtonStart.setText('PAUSE')
		elif (not provjeraButtonStart):
			self.timer.stop()
			provjeraButtonStart = not provjeraButtonStart
			self.pushButtonStart.setText('START')

	def timer_time(self):
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

		self.labelTimer.setText(time)

	def dodavanje_na(self, imeInputa):
		imeInputa.setText("N/A")

	# mjerenje vremena (mozda bi mogla biti smjena)
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
	def closeEvent(self, event):
		pitanjeExit = "Are you sure you want to exit the program?"
		odgovorExit = QtGui.QMessageBox.question(self, 'Exiting...', 
						pitanjeExit, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

		if odgovorExit == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def actionAbout_triggered(self):
		self.popAboutDialog.show()

	# unos u bazu
	def click_on_pushButtonSave_btn(self):
		pitanjeSave = "Are you sure you want to save the ticket #{0}?\nSeverity: {1}\nStatus: {2}\nDate: {3}\nName and last name: {4}\nCallback number: {5}\nZip code: {6}\nVersion: {7}\nNext steps: {8}\nDescription of the problem: {9}".format(self.lineEditIncident.text(), self.comboBoxSeverity.currentText(),self.comboBoxStatus.currentText(), self.lineEditDatum.text(), self.lineEditImePrezime.text(), self.lineEditBrojTelefona.text(), self.lineEditZipCode.text(), self.plainTextEditVersions.toPlainText(), self.plainTextEditNextSteps.toPlainText(), self.plainTextEditDescriptionProblem.toPlainText())
		odgovorSave = QtGui.QMessageBox.question(self, "{0}:{1}:{2}".format(h, m, s), 
						pitanjeSave, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

		if (odgovorSave == QtGui.QMessageBox.Yes):
			connection = sqlite3.connect("baza_main.db")
			c = connection.cursor()

			connection.execute("""
						INSERT INTO 
							ticket_info 
						VALUES
							(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
						""", (None, str(self.lineEditIncident.text()), str(self.comboBoxSeverity.currentText()), str(self.comboBoxStatus.currentText()), str(self.lineEditDatum.text()), str(self.lineEditImePrezime.text()), str(self.lineEditBrojTelefona.text()), str(self.lineEditZipCode.text()), str(self.lineEditEmail.text()), str(self.plainTextEditVersions.toPlainText()), str(self.lineEditHasSiteEverCalled.text()), str(self.lineEditDidItEverWork.text()), str(self.lineEditWhenDidItStop.text()), str(self.lineEditChangesMade.text()), str(self.lineEditHowManyTermLocation.text()), str(self.lineEditHowManyTermDown.text()), str(self.lineEditAnyAffected.text()), str(self.lineEditScreenshotsAttached.text()), str(self.lineEditModelSerial.text()), str(self.lineEditAlternativeMethod.text()), str(self.plainTextEditNextSteps.toPlainText()), str(self.plainTextEditDescriptionProblem.toPlainText()), str(self.plainTextEditReporoductionTroubleshooting.toPlainText()), h, m, s))
			connection.commit()
			connection.close()
			self.clear_all_fields()
		else:
			pass

	def click_on_pushButtonCopyToClipboard(self):
		sadrzajZaCb = "Versions:\n{0}\nDescription:\n{1}\nTroubleshoting steps:\n{2}\nNext steps:\n{3}".format(self.plainTextEditVersions.toPlainText(), self.plainTextEditDescriptionProblem.toPlainText(), self.plainTextEditReporoductionTroubleshooting.toPlainText(), self.plainTextEditNextSteps.toPlainText())
		cb = QtGui.QApplication.clipboard()
		cb.clear(mode = cb.Clipboard)
		cb.setText(sadrzajZaCb, mode = cb.Clipboard)

	# vracanje copyToClipboard i save buttona na "clickable" kad su inputi popunjeni
	def enable_pushButtonCopyToClipboard_btn(self):
		if (len(self.plainTextEditVersions.toPlainText()) and len(self.lineEditHasSiteEverCalled.text()) and len(self.lineEditDidItEverWork.text()) and len(self.lineEditWhenDidItStop.text()) and len(self.lineEditChangesMade.text()) and len(self.lineEditHowManyTermLocation.text()) and len(self.lineEditHowManyTermDown.text()) and len(self.lineEditAnyAffected.text()) and len(self.lineEditScreenshotsAttached.text()) and len(self.lineEditModelSerial.text()) and len(self.lineEditAlternativeMethod.text()) and len(self.plainTextEditNextSteps.toPlainText()) and len(self.plainTextEditDescriptionProblem.toPlainText()) and len(self.plainTextEditReporoductionTroubleshooting.toPlainText()) > 0):
			self.pushButtonCopyToClipboard.setDisabled(False)
			self.pushButtonSave.setDisabled(False)
			
		else:
			self.pushButtonCopyToClipboard.setDisabled(True)
			self.pushButtonSave.setDisabled(True)

	# brisanje svih inputa na klik butona clear all fields i save buttona
	def clear_all_fields(self):
		self.plainTextEditVersions.clear()
		self.lineEditHasSiteEverCalled.clear()
		self.lineEditDidItEverWork.clear()
		self.lineEditWhenDidItStop.clear()
		self.lineEditChangesMade.clear()
		self.lineEditHowManyTermLocation.clear()
		self.lineEditHowManyTermDown.clear()
		self.lineEditAnyAffected.clear()
		self.lineEditScreenshotsAttached.clear()
		self.lineEditModelSerial.clear()
		self.lineEditAlternativeMethod.clear()
		self.plainTextEditNextSteps.clear()
		self.plainTextEditDescriptionProblem.clear()
		self.plainTextEditReporoductionTroubleshooting.clear()
		self.lineEditIncident.clear()
		self.comboBoxSeverity.clear()
		self.comboBoxSeverity.addItems(['Sev 1', 'Sev 2', 'Sev 3'])
		self.comboBoxStatus.clear()
		self.comboBoxStatus.addItems(['Open', 'Closed', 'WFC', 'Escalated'])
		self.lineEditImePrezime.clear()
		self.lineEditBrojTelefona.clear()
		self.lineEditZipCode.clear()
		self.lineEditSiteKey.clear()
		self.lineEditEmail.clear()
		self.timer_reset()

	# input-i koji su required, postaju odredjene boje da USER zna da je taj input required
	# def promjena_boje_inputa(self):
	# 	self.prvi_input.textChanged.connect(lambda boja: self.prvi_input.setStyleSheet(
	# 	"QWidget { background-color: %s}" % ('rgb(255, 255, 255)' if boja else 'rgb(212, 60, 60)')))
	# 	self.drugi_input.textChanged.connect(lambda boja: self.drugi_input.setStyleSheet(
	# 	"QWidget { background-color: %s}" % ('rgb(255, 255, 255)' if boja else 'rgb(212, 60, 60)')))
		#ostali inputi idu ovdje

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())