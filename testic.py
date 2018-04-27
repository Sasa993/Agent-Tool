import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "gui_fajl.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.button.clicked.connect(self.testirana_funkcija)

	def testirana_funkcija(self):
		kita = str(self.prvi_input.text())
		kita2 = str(self.drugi_input.text())

		# print("Prvo je {} a drugo je {}".format(kita, kita2))
		self.output_label.setText(kita + " " + kita2)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())