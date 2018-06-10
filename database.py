import sqlite3
import datetime

vrijeme = datetime.date.today().strftime("%m/%d/%Y")

def testic():
	conn = sqlite3.connect("baza_main.db")
	c = conn.cursor()

	# c.execute("CREATE TABLE ticket_info (id_ticket_info INTEGER PRIMARY KEY AUTOINCREMENT, incident_number INTEGER NOT NULL, severity TEXT NOT NULL, status TEXT NOT NULL, datum DATE NOT NULL, day INT, month INT, year INT, site_key TEXT NOT NULL, name_last_name TEXT NOT NULL, callback_number TEXT NOT NULL, zip_code TEXT NOT NULL, email TEXT NOT NULL, versions TEXT NOT NULL, has_site_ever_called TEXT NOT NULL, did_it_work TEXT NOT NULL, when_did_it_stop TEXT NOT NULL, changes_made TEXT NOT NULL, how_many_term_location TEXT NOT NULL, how_many_term_down TEXT NOT NULL, any_spec_term TEXT NOT NULL, screenshots_attached TEXT NOT NULL, model_serial_number TEXT NOT NULL, alternative_method TEXT NOT NULL, next_steps TEXT NOT NULL, description_problem TEXT NOT NULL, reporoduction_and_ts TEXT NOT NULL, vrijeme_trajanja_poziva_h INTEGER NOT NULL, vrijeme_trajanja_poziva_m INTEGER NOT NULL, vrijeme_trajanja_poziva_s INTEGER NOT NULL)")
	# c.execute("DROP TABLE shifts")
	# c.execute("INSERT INTO ticket_info (id_ticket_info, incident_number, severity, status, datum, site_key, name_last_name, callback_number, zip_code, email, versions, has_site_ever_called, did_it_work, when_did_it_stop, changes_made, how_many_term_location, how_many_term_down, any_spec_term, screenshots_attached, model_serial_number, alternative_method, next_steps, description_problem, reporoduction_and_ts, vrijeme_trajanja_poziva_h, vrijeme_trajanja_poziva_m, vrijeme_trajanja_poziva_s) SELECT id_ticket_info, incident_number, severity, status, datum, site_key, name_last_name, callback_number, zip_code, email, versions, has_site_ever_called, did_it_work, when_did_it_stop, changes_made, how_many_term_location, how_many_term_down, any_spec_term, screenshots_attached, model_serial_number, alternative_method, next_steps, description_problem, reporoduction_and_ts, vrijeme_trajanja_poziva_h, vrijeme_trajanja_poziva_m, vrijeme_trajanja_poziva_s FROM TempOldTable")
	
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