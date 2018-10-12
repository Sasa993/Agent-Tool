import sqlite3
import datetime

vrijeme = datetime.date.today().strftime("%m/%d/%Y")

def testic():
	conn = sqlite3.connect("baza_main.db")
	c = conn.cursor()

	# KATEGORIJA
	# c.execute("CREATE TABLE kategorija (id_kategorije INTEGER PRIMARY KEY AUTOINCREMENT, naziv_kategorije TEXT NOT NULL)")
	# c.execute("DROP TABLE kategorija")
	# c.execute("INSERT INTO kategorija VALUES(NULL, 'Other')")
	# c.execute("UPDATE kategorija SET naziv_kategorije='End Of Day' WHERE id_kategorije=8")
	
	# c.execute("CREATE TABLE ticket_info (id_ticket_info INTEGER PRIMARY KEY AUTOINCREMENT, incident_number INTEGER NOT NULL, severity TEXT NOT NULL, status TEXT NOT NULL, datum DATE NOT NULL, day INT, month INT, year INT, site_key TEXT NOT NULL, name_last_name TEXT NOT NULL, callback_number TEXT NOT NULL, zip_code TEXT NOT NULL, email TEXT NOT NULL, versions TEXT NOT NULL, has_site_ever_called TEXT NOT NULL, did_it_work TEXT NOT NULL, when_did_it_stop TEXT NOT NULL, changes_made TEXT NOT NULL, how_many_term_location TEXT NOT NULL, how_many_term_down TEXT NOT NULL, any_spec_term TEXT NOT NULL, screenshots_attached TEXT NOT NULL, model_serial_number TEXT NOT NULL, alternative_method TEXT NOT NULL, next_steps TEXT NOT NULL, description_problem TEXT NOT NULL, reporoduction_and_ts TEXT NOT NULL, vrijeme_trajanja_poziva_h INTEGER NOT NULL, vrijeme_trajanja_poziva_m INTEGER NOT NULL, vrijeme_trajanja_poziva_s INTEGER NOT NULL, kategorija INTEGER NULL, FOREIGN KEY(kategorija) REFERENCES kategorija(id_kategorije))")
	# c.execute("DROP TABLE ticket_info")
	# c.execute("INSERT INTO ticket_info (id_ticket_info, incident_number, severity, status, datum, site_key, name_last_name, callback_number, zip_code, email, versions, has_site_ever_called, did_it_work, when_did_it_stop, changes_made, how_many_term_location, how_many_term_down, any_spec_term, screenshots_attached, model_serial_number, alternative_method, next_steps, description_problem, reporoduction_and_ts, vrijeme_trajanja_poziva_h, vrijeme_trajanja_poziva_m, vrijeme_trajanja_poziva_s) SELECT id_ticket_info, incident_number, severity, status, datum, site_key, name_last_name, callback_number, zip_code, email, versions, has_site_ever_called, did_it_work, when_did_it_stop, changes_made, how_many_term_location, how_many_term_down, any_spec_term, screenshots_attached, model_serial_number, alternative_method, next_steps, description_problem, reporoduction_and_ts, vrijeme_trajanja_poziva_h, vrijeme_trajanja_poziva_m, vrijeme_trajanja_poziva_s FROM TempOldTable")

	# UPDATE-OVANJE TICKET_INFO TABELE SA KATEGORIJOM
	# kveri = c.execute("SELECT description_problem FROM ticket_info")
	# conn.commit()
	# brojac = 1

	# kveri = kveri.fetchall()
	# for x in kveri:
	# 	for y in x:
	# 		glavniString = y.lower()
	# 		if (" network" in glavniString) or (" isp" in glavniString) or ("router" in glavniString) or ("firewall" in glavniString) or ("modem" in glavniString) or ("ip address" in glavniString):
	# 			rezultat = 1
	# 		elif (" red " in glavniString) or ("in red" in glavniString) or ("redundancy" in glavniString) or ("looking for file server" in glavniString) or ("looking for fs" in glavniString)  or ("looking for fileserver" in glavniString) or ("looking for master" in glavniString) or ("find master" in glavniString) or ("find fileserver" in glavniString) or ("find fs" in glavniString) or ("determining fs" in glavniString) or ("determining file server" in glavniString) or ("make fs" in glavniString) or ("make file server" in glavniString) or ("locate fs" in glavniString) or ("locate file server" in glavniString) or ("locate master" in glavniString):
	# 			rezultat = 2
	# 		elif ("edc" in glavniString) or ("authorize" in glavniString) or ("authorizing" in glavniString) or ("credit card" in glavniString) or (" cc " in glavniString) or ("spooldown" in glavniString) or ("refund" in glavniString) or (" tip " in glavniString) or ("batch " in glavniString) or ("process cc" in glavniString) or ("process ccs" in glavniString) or ("ccs process" in glavniString) or ("cc process" in glavniString) or ("cc stuck" in glavniString) or ("ccs stuck" in glavniString):
	# 			rezultat = 3
	# 		elif ("install" in glavniString):
	# 			rezultat = 4
	# 		elif ("printer" in glavniString) or ("com port" in glavniString) or ("printing" in glavniString):
	# 			rezultat = 5
	# 		elif ("reoccurring" in glavniString):
	# 			rezultat = 6
	# 		elif ("cash drawer" in glavniString) or (" cd " in glavniString) or ("cash register" in glavniString):
	# 			rezultat = 7
	# 		elif ("end of day" in glavniString) or (" eod " in glavniString) or ("waiting for permission to resume" in glavniString):
	# 			rezultat = 8
	# 		elif ("aloha manager" in glavniString) or (" am " in glavniString) or ("cfc " in glavniString) or ("configuration center" in glavniString) or ("am password reset" in glavniString) or ("login to am" in glavniString) or ("login to aloha manager" in glavniString) or ("login to cfc" in glavniString) or ("adding an item" in glavniString) or ("adding item" in glavniString) or ("add an item" in glavniString) or ("add item" in glavniString) or ("happy hour" in glavniString) or ("in am" in glavniString) or ("on am" in glavniString):
	# 			rezultat = 9
	# 		elif ("cable" in glavniString) or ("hardware" in glavniString) or ("damaged" in glavniString):
	# 			rezultat = 10
	# 		elif (" date " in glavniString) or ("incorrect time" in glavniString) or ("different time" in glavniString) or ("time correction" in glavniString):
	# 			rezultat = 11
	# 		elif ("windows" in glavniString) or ("operating system" in glavniString):
	# 			rezultat = 12
	# 		elif ("ato " in glavniString) or ("takeout" in glavniString) or ("online order" in glavniString) or ("online ordering" in glavniString):
	# 			rezultat = 13
	# 		elif ("loyalty" in glavniString) or ("gift card" in glavniString) or (" gc " in glavniString):
	# 			rezultat = 14
	# 		elif ("orderman" in glavniString) or ("aloha mobile" in glavniString):
	# 			rezultat = 15
	# 		elif ("discrepancy" in glavniString) or ("different amount" in glavniString) or ("missing $" in glavniString) or ("missing money" in glavniString) or ("discrepancies" in glavniString):
	# 			rezultat = 16
	# 		elif ("aloha kitchen" in glavniString) or ("kitchen screen" in glavniString) or (" ak " in glavniString):
	# 			rezultat = 17
	# 		else:
	# 			rezultat = 18

	# 		c.execute("UPDATE ticket_info SET kategorija=? WHERE id_ticket_info=?", (rezultat, brojac))
	# 		print("{0}.Rezultat je {1}".format(brojac, rezultat))
	# 		conn.commit()
	# 		brojac += 1
	# UPDATE-OVANJE TICKET_INFO TABELE SA KATEGORIJOM END
	
	# c.execute("CREATE TABLE shifts (id_shifts INTEGER PRIMARY KEY, shift_ends TEXT, shift_last_changed DATE, action_name TEXT)")
	# c.execute("INSERT INTO shifts VALUES(NULL, strftime('%H:%M:%S', '06:00:00'), strftime('%m/%d/%Y', 'now'), 'action06')")

	# c.execute("INSERT INTO ticket_info (id_ticket_info, incident_number, severity, status, datum, day, month, year, site_key, name_last_name, callback_number, zip_code, email, versions, has_site_ever_called, did_it_work, when_did_it_stop, changes_made, how_many_term_location, how_many_term_down, any_spec_term, screenshots_attached, model_serial_number, alternative_method, next_steps, description_problem, reporoduction_and_ts, vrijeme_trajanja_poziva_h, vrijeme_trajanja_poziva_m, vrijeme_trajanja_poziva_s) SELECT id_ticket_info, incident_number, severity, status, datum, strftime('%d', 'Datum'), strftime('%m', 'Datum'), strftime('%Y', 'Datum'), site_key, name_last_name, callback_number, zip_code, email, versions, has_site_ever_called, did_it_work, when_did_it_stop, changes_made, how_many_term_location, how_many_term_down, any_spec_term, screenshots_attached, model_serial_number, alternative_method, next_steps, description_problem, reporoduction_and_ts, vrijeme_trajanja_poziva_h, vrijeme_trajanja_poziva_m, vrijeme_trajanja_poziva_s FROM TempOldTable")

	# c.execute("UPDATE ticket_info set day = strftime('%d', 'datum')")
	# c.execute("CREATE TABLE test (id_test INTEGER PRIMARY KEY AUTOINCREMENT, ime TEXT NOT NULL)")
	# c.execute("ALTER TABLE SVE ADD COLUMN 'GODISTE' INTEGER NULL DEFAULT 1800")
	# c.execute("DROP TABLE ticket_info")
	# c.execute("UPDATE users2 set ime = 'Saskonja' where  = 3")
	# c.execute("INSERT INTO aaa VALUES(strftime('%m/%d/%Y', 'now'))")
	# c.execute("INSERT INTO test(ime) VALUES('Nikola')")
	# c.execute("INSERT INTO test VALUES(NULL, 'Drako')")
	# testic = "zIVKA"
	# c.execute("""
	# 	INSERT INTO
	# 		test
	# 	VALUES
	# 		(?, ?)
	# 	""", (None,testic))

	# rezultat = c.execute("SELECT * FROM ticket_info")

	# for x in rezultat:
	# 	print(x)

	conn.commit()
	conn.close()

testic()