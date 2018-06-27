import sys
import sqlite3
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QLineEdit
from gui_glavni import Ui_MainWindow
from gui_about import Ui_aboutDialog
from gui_testic import Ui_testWidget
from gui_selektovani import Ui_selektovaniId
import datetime

bazica = "baza_main.db"

s = 0
m = 0
h = 0

conn = sqlite3.connect(bazica)
c = conn.cursor()

c.execute("SELECT shift_ends FROM shifts")
countdownKrajSmjene = c.fetchone()[0]
conn.commit()

c.execute("SELECT shift_last_changed from shifts")
menuShiftTip = c.fetchone()[0]
conn.commit()

conn.close()

provjeraButtonStart = True

lista = []

class aboutDialog(QtGui.QDialog, Ui_aboutDialog):
	def __init__(self, parent = None):
		QtGui.QDialog.__init__(self, parent)
		flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setupUi(self)
		self.about_btn.clicked.connect(self.click_on_about_btn)

	def click_on_about_btn(self):
		self.close()

# widget za ispis iz baze (Table)
class Ui_testWidget(QtGui.QWidget, Ui_testWidget):
	def __init__(self, parent = None):
		# super(Ui_testWidget, self).__init__(parent)
		QtGui.QWidget.__init__(self, parent)
		flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setupUi(self)

		self.pushButtonRefresh.clicked.connect(self.click_on_pushButtonRefreh)
		self.pushButtonSelektovano.clicked.connect(self.selektovano)
		self.pushButtonSearch.clicked.connect(self.novi_ispis)

		# self.popSelektovaniId = Ui_selektovaniId()

		# self.kurcina()
		self.ispis_iz_baze()
	# refresh ispisa nakon novog unosa
	def click_on_pushButtonRefreh(self):
		self.tableWidgetIspisIzBaze.clearContents()
		self.tableWidgetIspisIzBaze.setRowCount(0)
		self.ispis_iz_baze()

	def selektovano(self):
		global lista

		for x in self.tableWidgetIspisIzBaze.selectedItems():
			lista.append(x.text())

		#print(lista[0])

		self.popSelektovaniId = Ui_selektovaniId()
		self.popSelektovaniId.show()

	def ispis_iz_baze(self):
		conn = sqlite3.connect(bazica)
		c = conn.cursor()

		testni_kveri = c.execute('SELECT * FROM ticket_info')
		conn.commit()

		for x in testni_kveri:
			# self.toolBox.addItem(QtGui.QPlainTextEdit("{0}h {1}min {2}sec\nZip code: {3}\n\n{4}\nSite/Tree/Key #: {5}\nDate / Time issue occurs: {6}\n\nPoint of Contact (First and Last name): {7}\nSite/Point of Contact Phone#: {8}\nSite/Point of Contact Email: {9}\n\nDescription of the Problem:\n{10}\n\nHas site ever called support for the same issue?: {11}\n\nDid it ever work?: {12}\n\nWhen did it stop working: {13}\nChanges made around that time: {14}\n\nHow many terminals on location: {15}\nHow many terminals are down: {16}\nAre any of the affected terminals specialty terminals?: {17}\n\nReproduction and Troubleshooting steps taken to resolve:\n\n{18}\n\nScreen shots attached (if applicable): {19}\nModel & S/N (if hardware related): {20}\nAlternative method that will be used by the site: {21}\n\n***Next Steps for next contact:\n{22}".format(x[24], x[25], x[26], x[8], x[10], x[5], x[4], x[6], x[7], x[9], x[22], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[23], x[18], x[19], x[20], x[21])), "{0}. Ticket: #{1}    Severity: {2}    Status:{3}    Date:{4}".format(x[0], x[1], x[2], x[3], x[4]))

			# da bi table funkcionisao, moramo dodavati row za svaki
			rowPosition = self.tableWidgetIspisIzBaze.rowCount()
			self.tableWidgetIspisIzBaze.insertRow(rowPosition)
			
			item = QtGui.QTableWidgetItem()
			# da bi ID bio INTEGER da se moze sortirati normalno
			item.setData(QtCore.Qt.EditRole, x[0])
			item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			item1 = QtGui.QTableWidgetItem("{0}".format(x[1]))
			item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			item2 = QtGui.QTableWidgetItem("{0}".format(x[2]))
			item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			item3 = QtGui.QTableWidgetItem("{0}".format(x[3]))
			item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			item4 = QtGui.QTableWidgetItem("{0}".format(x[4]))
			item4.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

			self.tableWidgetIspisIzBaze.setItem(rowPosition, 0, item)
			self.tableWidgetIspisIzBaze.setItem(rowPosition, 1, item1)
			self.tableWidgetIspisIzBaze.setItem(rowPosition, 2, item2)
			self.tableWidgetIspisIzBaze.setItem(rowPosition, 3, item3)
			self.tableWidgetIspisIzBaze.setItem(rowPosition, 4, item4)

		datumSada = str(datetime.date.today().strftime("%m/%d/%Y"))

		# kveri za ispis broja tiketa za danas
		hihi=c.execute("SELECT COUNT(*) FROM ticket_info WHERE datum = '{0}'".format(str(datetime.date.today().strftime("%m/%d/%Y"))))
		conn.commit()
		self.labelBrojTiketaDanas.setText("{0} ticket(s)".format(str(c.fetchone()[0])))

		# kveri za ispis broja tiketa za trenutni mjesec
		c.execute("SELECT COUNT(*) FROM ticket_info WHERE month = '{0}'".format(datetime.datetime.strptime(datumSada, "%m/%d/%Y").month))
		conn.commit()
		self.labelBrojTiketaMjesec.setText("{0} ticket(s)".format(str(c.fetchone()[0])))

		# kveriji za srednju vrijednost trajanja svih poziva
		brojTiketa = c.execute("SELECT COUNT(*) FROM ticket_info")
		brojTiketa = brojTiketa.fetchone()[0]
		trajanjePozivaS = c.execute("SELECT SUM(vrijeme_trajanja_poziva_s) FROM ticket_info")
		trajanjePozivaS = trajanjePozivaS.fetchone()[0]
		trajanjePozivaM = c.execute("SELECT SUM(vrijeme_trajanja_poziva_m) FROM ticket_info")
		trajanjePozivaM = trajanjePozivaM.fetchone()[0] * 60
		trajanjePozivaH = c.execute("SELECT SUM(vrijeme_trajanja_poziva_h) FROM ticket_info")
		trajanjePozivaH = trajanjePozivaH.fetchone()[0] * 60 * 60

		trajanjeUkupno = trajanjePozivaS + trajanjePozivaM + trajanjePozivaH

		finalni = trajanjeUkupno / brojTiketa
		finalniSatic = int(finalni / 60 / 60)
		finalniMinutic = int(finalni / 60)
		finalniSekundic = finalni % 60

		finalnaSrednjaVrijednost = "{0:02d}:{1:02d}:{2:02d}".format(finalniSatic, finalniMinutic, int(finalniSekundic))

		conn.commit()
		self.labelSrednjaVrijednostDuzine.setText(finalnaSrednjaVrijednost)

		conn.close()

	def novi_ispis(self):
		conn = sqlite3.connect(bazica)
		c = conn.cursor()

		sandra = self.lineEditSearch.text()
		sandra = '%' + sandra + '%'

		testni_kveri = c.execute("SELECT * FROM ticket_info WHERE description_problem LIKE ? OR incident_number LIKE ?", (sandra, sandra))

		conn.commit()

		self.tableWidgetIspisIzBaze.clearContents()
		self.tableWidgetIspisIzBaze.setRowCount(0)

		for x in testni_kveri:
			# self.toolBox.addItem(QtGui.QPlainTextEdit("{0}h {1}min {2}sec\nZip code: {3}\n\n{4}\nSite/Tree/Key #: {5}\nDate / Time issue occurs: {6}\n\nPoint of Contact (First and Last name): {7}\nSite/Point of Contact Phone#: {8}\nSite/Point of Contact Email: {9}\n\nDescription of the Problem:\n{10}\n\nHas site ever called support for the same issue?: {11}\n\nDid it ever work?: {12}\n\nWhen did it stop working: {13}\nChanges made around that time: {14}\n\nHow many terminals on location: {15}\nHow many terminals are down: {16}\nAre any of the affected terminals specialty terminals?: {17}\n\nReproduction and Troubleshooting steps taken to resolve:\n\n{18}\n\nScreen shots attached (if applicable): {19}\nModel & S/N (if hardware related): {20}\nAlternative method that will be used by the site: {21}\n\n***Next Steps for next contact:\n{22}".format(x[24], x[25], x[26], x[8], x[10], x[5], x[4], x[6], x[7], x[9], x[22], x[11], x[12], x[13], x[14], x[15], x[16], x[17], x[23], x[18], x[19], x[20], x[21])), "{0}. Ticket: #{1}    Severity: {2}    Status:{3}    Date:{4}".format(x[0], x[1], x[2], x[3], x[4]))

			# da bi table funkcionisao, moramo dodavati row za svaki
			rowPosition = self.tableWidgetIspisIzBaze.rowCount()
			self.tableWidgetIspisIzBaze.insertRow(rowPosition)
			
			item = QtGui.QTableWidgetItem()
			# da bi ID bio INTEGER da se moze sortirati normalno
			item.setData(QtCore.Qt.EditRole, x[0])
			item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			item1 = QtGui.QTableWidgetItem("{0}".format(x[1]))
			item1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			item2 = QtGui.QTableWidgetItem("{0}".format(x[2]))
			item2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			item3 = QtGui.QTableWidgetItem("{0}".format(x[3]))
			item3.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
			item4 = QtGui.QTableWidgetItem("{0}".format(x[4]))
			item4.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

			self.tableWidgetIspisIzBaze.setItem(rowPosition, 0, item)
			self.tableWidgetIspisIzBaze.setItem(rowPosition, 1, item1)
			self.tableWidgetIspisIzBaze.setItem(rowPosition, 2, item2)
			self.tableWidgetIspisIzBaze.setItem(rowPosition, 3, item3)
			self.tableWidgetIspisIzBaze.setItem(rowPosition, 4, item4)

		conn.close()

class Ui_selektovaniId(QtGui.QWidget, Ui_selektovaniId):
	def __init__(self, parent = None):
		QtGui.QWidget.__init__(self, parent)
		flags = QtCore.Qt.Drawer | QtCore.Qt.WindowStaysOnTopHint
		self.setWindowFlags(flags)
		self.setupUi(self)
		self.uradi_nesto()

	def uradi_nesto(self):
		global lista

		conn = sqlite3.connect(bazica)
		c = conn.cursor()

		neki_kveri = c.execute("SELECT * FROM ticket_info WHERE id_ticket_info = '{0}'".format(lista[0]))

		for x in neki_kveri:
			self.plainTextEditOutput.setPlainText("{0}\nSite/Tree/Key #: {1}\nDate / Time issue occurs: {2}\n\nPoint of Contact (First and Last name): {3}\nSite/Point of Contact Phone#: {4}\nSite/Point of Contact Email: {5}\n\nDescription of the Problem:\n{6}\n\nHas site ever called support for the same issue?: {7}\n\nDid it ever work?: {8}\n\nWhen did it stop working: {9}\nChanges made around that time: {10}\n\nHow many terminals on location: {11}\nHow many terminals are down: {12}\nAre any of the affected terminals specialty terminals?: {13}\n\nReproduction and Troubleshooting steps taken to resolve:\n\n{14}\n\nScreen shots attached (if applicable): {15}\nModel & S/N (if hardware related): {16}\nAlternative method that will be used by the site: {17}\n\n***Next Steps for next contact:\n{18}".format(x[13], x[8], x[4], x[9], x[10], x[12], x[25], x[14], x[15], x[16], x[17], x[18], x[19], x[20], x[26], x[21], x[22], x[23], x[24]))
			self.labelIncidentNumber.setText(str(x[1]))
			self.labelVrijeme.setText(str("{0}h {1}min {2}sec".format(x[27], x[28], x[29])))
			self.labelSeverity.setText(x[2])
			self.labelStatus.setText(x[3])
			self.setWindowTitle(x[25])

		conn.commit()
		conn.close()

		# brisanje svih clanova liste ____
		lista.clear()

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)

		# pushButtonCopyToClipboard i pushButtonSave disabling
		# self.pushButtonClearAllFields.setStyleSheet("QPushButton:hover { color: white }")
		self.pushButtonCopyToClipboard.setDisabled(True)
		self.pushButtonSave.setDisabled(True)
		self.lineEditImePrezime.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditBrojTelefona.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditEmail.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditSiteKey.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
		self.lineEditDatum.textChanged.connect(self.enable_pushButtonCopyToClipboard_btn)
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

		#shift changes
		self.testiramokitic()

		self.menuShift.setToolTip("Last changed on {0}".format(menuShiftTip))
		self.action06.triggered.connect(lambda: self.promjena_smjene("08:00:00", self.action06, "action06"))
		self.action14.triggered.connect(lambda: self.promjena_smjene("16:00:00", self.action14, "action14"))
		self.action15.triggered.connect(lambda: self.promjena_smjene("17:00:00", self.action15, "action15"))
		self.action16.triggered.connect(lambda: self.promjena_smjene("18:00:00", self.action16, "action16"))
		self.action18.triggered.connect(lambda: self.promjena_smjene("20:00:00", self.action18, "action18"))
		self.action22.triggered.connect(lambda: self.promjena_smjene("00:00:00", self.action22, "action22"))

		self.actionAbout.triggered.connect(self.actionAbout_triggered)
		self.popAboutDialog = aboutDialog()

		self.actionTestic.triggered.connect(self.actionTestic_triggered)
		self.popTestic = Ui_testWidget()

		# timer
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.timer_time)
		self.pushButtonStart.clicked.connect(self.timer_start)
		self.pushButtonReset.clicked.connect(self.timer_reset)

		self.timer2 = QtCore.QTimer()
		self.timer2.timeout.connect(self.countdown)
		self.timer2.start(1000)

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

	def testiramokitic(self):
		conn = sqlite3.connect(bazica)
		c = conn.cursor()

		c.execute("SELECT action_name from shifts")
		kitic = c.fetchone()[0]
		conn.commit()
		if (kitic == "action06"):
			self.action06.setChecked(True)
		elif (kitic == "action14"):
			self.action14.setChecked(True)
		elif (kitic == "action15"):
			self.action15.setChecked(True)
		elif (kitic == "action16"):
			self.action16.setChecked(True)
		elif (kitic == "action18"):
			self.action18.setChecked(True)
		else:
			self.action22.setChecked(True)

		conn.close()

	def timer_reset(self):
		global s, m, h, provjeraButtonStart

		self.timer.stop()
		provjeraButtonStart = True
		self.pushButtonStart.setChecked(False)

		s = 0
		m = 0
		h = 0
 
		time = "{0:02d}:{1:02d}:{2:02d}".format(h,m,s)

		self.labelTimer.setText(time)
		self.labelTimer.setStyleSheet('color: rgb(0, 0, 0)')
		self.labelTimer.setFont(QtGui.QFont("MS Shell Dlg 2", 20, weight=QtGui.QFont.Normal))

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

		time = "{0:02d}:{1:02d}:{2:02d}".format(h, m, s)

		self.labelTimer.setText(time)

		# promjena boje timera kad predje 30 min, ili sat
		if (m == 30 and h == 0):
			self.labelTimer.setStyleSheet('color: rgb(255, 165, 0)')
		if (h == 1):
			self.labelTimer.setStyleSheet('color: rgb(255, 69, 0)')
			self.labelTimer.setFont(QtGui.QFont("MS Shell Dlg 2", 20, weight=QtGui.QFont.Bold))

	def dodavanje_na(self, imeInputa):
		imeInputa.setText("N/A")

	def countdown(self):
		trenutnoVrijeme = str(datetime.datetime.now().strftime("%H:%M:%S"))
		countdownPreostaloVrijeme = datetime.datetime.strptime(countdownKrajSmjene, "%H:%M:%S") - datetime.datetime.strptime(trenutnoVrijeme, "%H:%M:%S")
		#[-8:] koristimo da uzmemo posljednjih 8 karaktera stringa, da bi izbjegli -1 days (sugavi timedelta)
		self.labelShiftEnds.setText(str(countdownPreostaloVrijeme)[-8:])

	# built-in event kada se ide na X da se close-a window
	def closeEvent(self, event):
		pitanjeExit = "Are you sure you want to exit the program?"
		odgovorExit = QtGui.QMessageBox.question(self, 'Exiting...', 
						pitanjeExit, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

		if odgovorExit == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def promjena_smjene(self, x, y, z):
		global countdownKrajSmjene
		countdownKrajSmjene = str(datetime.datetime.strptime(x, "%H:%M:%S").time())
		conn = sqlite3.connect(bazica)
		c = conn.cursor()
		# mogao sam odraditi sa INSERT ali ovako ne moramo traziti posljednju kolonu tabele i bolja je optimizacija DB-a
		c.execute("UPDATE shifts set shift_ends = ?, shift_last_changed = ?, action_name = ? WHERE id_shifts = 1", (countdownKrajSmjene, str(datetime.date.today().strftime("%m/%d/%Y")), z))

		conn.commit()
		conn.close()

		self.action06.setChecked(False)
		self.action14.setChecked(False)
		self.action15.setChecked(False)
		self.action16.setChecked(False)
		self.action18.setChecked(False)
		self.action22.setChecked(False)

		y.setChecked(True)

	def actionAbout_triggered(self):
		self.popAboutDialog.show()

	def actionTestic_triggered(self):
		self.popTestic.show()

	# unos u bazu
	def click_on_pushButtonSave_btn(self):
		pitanjeSave = "Are you sure you want to save the ticket #{0}?\nSeverity: {1}\nStatus: {2}\nDate: {3}\nName and last name: {4}\nCallback number: {5}\nZip code: {6}\nVersion: {7}\nNext steps: {8}\nDescription of the problem: {9}".format(self.lineEditIncident.text(), self.comboBoxSeverity.currentText(),self.comboBoxStatus.currentText(), self.lineEditDatum.text(), self.lineEditImePrezime.text(), self.lineEditBrojTelefona.text(), self.lineEditZipCode.text(), self.plainTextEditVersions.toPlainText(), self.plainTextEditNextSteps.toPlainText(), self.plainTextEditDescriptionProblem.toPlainText())
		odgovorSave = QtGui.QMessageBox.question(self, "{0}:{1}:{2}".format(h, m, s), 
						pitanjeSave, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

		if (odgovorSave == QtGui.QMessageBox.Yes):
			datumPojedinacni = datetime.datetime.strptime(self.lineEditDatum.text(), "%m/%d/%Y")
			connection = sqlite3.connect(bazica)
			c = connection.cursor()

			connection.execute("""
						INSERT INTO 
							ticket_info 
						VALUES
							(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
						""", (None, str(self.lineEditIncident.text()), str(self.comboBoxSeverity.currentText()), str(self.comboBoxStatus.currentText()), str(self.lineEditDatum.text()), datumPojedinacni.day, datumPojedinacni.month, datumPojedinacni.year, str(self.lineEditSiteKey.text()), str(self.lineEditImePrezime.text()), str(self.lineEditBrojTelefona.text()), str(self.lineEditZipCode.text()), str(self.lineEditEmail.text()), str(self.plainTextEditVersions.toPlainText()), str(self.lineEditHasSiteEverCalled.text()), str(self.lineEditDidItEverWork.text()), str(self.lineEditWhenDidItStop.text()), str(self.lineEditChangesMade.text()), str(self.lineEditHowManyTermLocation.text()), str(self.lineEditHowManyTermDown.text()), str(self.lineEditAnyAffected.text()), str(self.lineEditScreenshotsAttached.text()), str(self.lineEditModelSerial.text()), str(self.lineEditAlternativeMethod.text()), str(self.plainTextEditNextSteps.toPlainText()), str(self.plainTextEditDescriptionProblem.toPlainText()), str(self.plainTextEditReporoductionTroubleshooting.toPlainText()), h, m, s))
			connection.commit()
			connection.close()
			self.clear_all_fields()
		else:
			pass

	def click_on_pushButtonCopyToClipboard(self):
		sadrzajZaCb = "{0}\nSite/Tree/Key #: {1}\nDate / Time issue occurs: {2}\n\nPoint of Contact (First and Last name): {3}\nSite/Point of Contact Phone#: {4}\nSite/Point of Contact Email: {5}\n\nDescription of the Problem:\n{6}\n\nHas site ever called support for the same issue?: {7}\n\nDid it ever work?: {8}\n\nWhen did it stop working: {9}\nChanges made around that time: {10}\n\nHow many terminals on location: {11}\nHow many terminals are down: {12}\nAre any of the affected terminals specialty terminals?: {13}\n\nReproduction and Troubleshooting steps taken to resolve:\n\n{14}\n\nScreen shots attached (if applicable): {15}\nModel & S/N (if hardware related): {16}\nAlternative method that will be used by the site: {17}\n\n***Next Steps for next contact:\n{18}".format(self.plainTextEditVersions.toPlainText() ,self.lineEditSiteKey.text(), self.lineEditDatum.text(), self.lineEditImePrezime.text(), self.lineEditBrojTelefona.text(), self.lineEditEmail.text(), self.plainTextEditDescriptionProblem.toPlainText(), self.lineEditHasSiteEverCalled.text(), self.lineEditDidItEverWork.text(), self.lineEditWhenDidItStop.text(), self.lineEditChangesMade.text(), self.lineEditHowManyTermLocation.text(), self.lineEditHowManyTermDown.text(), self.lineEditAnyAffected.text(), self.plainTextEditReporoductionTroubleshooting.toPlainText(), self.lineEditScreenshotsAttached.text(), self.lineEditModelSerial.text(), self.lineEditAlternativeMethod.text(), self.plainTextEditNextSteps.toPlainText())

		cb = QtGui.QApplication.clipboard()
		cb.clear(mode = cb.Clipboard)
		cb.setText(sadrzajZaCb, mode = cb.Clipboard)

	# vracanje copyToClipboard i save buttona na "clickable" kad su inputi popunjeni
	def enable_pushButtonCopyToClipboard_btn(self):
		if (len(self.lineEditImePrezime.text()) and len(self.lineEditBrojTelefona.text()) and len(self.lineEditEmail.text()) and len(self.lineEditSiteKey.text()) and len(self.lineEditDatum.text()) and len(self.plainTextEditVersions.toPlainText()) and len(self.lineEditHasSiteEverCalled.text()) and len(self.lineEditDidItEverWork.text()) and len(self.lineEditWhenDidItStop.text()) and len(self.lineEditChangesMade.text()) and len(self.lineEditHowManyTermLocation.text()) and len(self.lineEditHowManyTermDown.text()) and len(self.lineEditAnyAffected.text()) and len(self.lineEditScreenshotsAttached.text()) and len(self.lineEditModelSerial.text()) and len(self.lineEditAlternativeMethod.text()) and len(self.plainTextEditNextSteps.toPlainText()) and len(self.plainTextEditDescriptionProblem.toPlainText()) and len(self.plainTextEditReporoductionTroubleshooting.toPlainText()) > 0):
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
		self.comboBoxStatus.addItems(['Active', 'Closed', 'WFC', 'Transferred', 'Escalated'])
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