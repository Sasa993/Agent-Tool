import sqlite3

def testic():
	conn = sqlite3.connect("baza.db")
	c = conn.cursor()

	# c.execute("CREATE TABLE users3 (id INTEGER PRIMARY KEY AUTOINCREMENT, ime TEXT NOT NULL, prezime TEXT NOT NULL)")
	# c.execute("ALTER TABLE SVE ADD COLUMN 'GODISTE' INTEGER NULL DEFAULT 1800")
	# c.execute("DROP TABLE users")
	# c.execute("UPDATE users2 set ime = 'Saskonja' where  = 3")

	# rezultat = c.execute("SELECT * FROM users2")

	# for x in rezultat:
	# 	print(x)

	conn.commit()
	conn.close()

testic()