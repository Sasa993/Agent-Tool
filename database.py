import sqlite3

def ispis_iz_baze():
	connection = sqlite3.connect("baza.db")

	rezultat = connection.execute("SELECT * FROM SVE")

	for data in rezultat:
		print("Ime: {0}\nPrezime: {1}".format(data[0], data[1]))

	connection.close()

ispis_iz_baze()