import sqlite3

def testic():
	conn = sqlite3.connect("baza.db")
	c = conn.cursor()

	# c.execute("CREATE TABLE test2 (id INTEGER PRIMARY KEY AUTOINCREMENT, ime TEXT NOT NULL, prezime TEXT DEFAULT '-')")
	# c.execute("ALTER TABLE SVE ADD COLUMN 'GODISTE' INTEGER NULL DEFAULT 1800")
	# c.execute("DROP TABLE users")
	# c.execute("UPDATE users2 set ime = 'Saskonja' where  = 3")
	c.execute("INSERT INTO test3 VALUES(NULL, ?, NULL)", ("Lesa"))

	# rezultat = c.execute("SELECT * FROM users2")

	# for x in rezultat:
	# 	print(x)

	conn.commit()
	conn.close()

testic()