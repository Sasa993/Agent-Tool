import sqlite3
import numpy as np
import matplotlib.pyplot as plt

bazica = "baza_main.db"

def StatusActionAll_triggered():
		conn = sqlite3.connect(bazica)
		c = conn.cursor()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = 'WFC'")
		brojWFC = c.fetchone()[0]
		conn.commit()
		
		c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = 'Transferred' OR status = 'Tranferred'")
		brojTransferred = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = 'Escalated'")
		brojEscalated = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = 'Closed'")
		brojClosed = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = 'Active' OR status = 'Open'")
		brojActive = c.fetchone()[0]
		conn.commit()

		fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

		data = [brojWFC, brojTransferred, brojEscalated, brojClosed, brojActive]
		ingredients = ['WFC', 'Transferred', 'Escalated', 'Closed', 'Active']


		def func(pct, allvals):
			absolute = int(pct/100.*np.sum(allvals))
			return "{:.1f}%\n({:d})".format(pct, absolute)


		wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
			textprops=dict(color="w"))

		ax.legend(wedges, ingredients,
			title="Status (All)",
			loc="center left",
			bbox_to_anchor=(1, 0, 0.5, 1))

		plt.setp(autotexts, size=8, weight="bold")

		ax.set_title("Status (All)")

		plt.show()
		conn.close()

def StatusActionYear_triggered(godina):
	conn = sqlite3.connect(bazica)
	c = conn.cursor()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = ? AND year = ?", ('WFC' ,godina))
	brojWFC = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (status = ? OR status = ?) AND year = ?", ('Transferred', 'Tranferred', godina))
	brojTransferred = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = ? AND year = ?", ('Escalated', godina))
	brojEscalated = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = ? AND year = ?", ('Closed', godina))
	brojClosed = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (status = ? OR status = ?) AND year = ?", ('Active', 'Open', godina))
	brojActive = c.fetchone()[0]
	conn.commit()

	fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

	data = [brojWFC, brojTransferred, brojEscalated, brojClosed, brojActive]
	ingredients = ['WFC', 'Transferred', 'Escalated', 'Closed', 'Active']


	def func(pct, allvals):
		absolute = int(pct/100.*np.sum(allvals))
		return "{:.1f}%\n({:d})".format(pct, absolute)


	wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
		textprops=dict(color="w"))

	ax.legend(wedges, ingredients,
		title="Status (Year {0})".format(godina),
		loc="center left",
		bbox_to_anchor=(1, 0, 0.5, 1))

	plt.setp(autotexts, size=8, weight="bold")

	ax.set_title("Status (Year {0})".format(godina))

	plt.show()
	conn.close()

def StatusActionMonth_triggered(godina, mjesec):
	conn = sqlite3.connect(bazica)
	c = conn.cursor()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = ? AND year = ? AND month = ?", ('WFC' ,godina, mjesec))
	brojWFC = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (status = ? OR status = 'Tranferred') AND year = ? AND month = ?", ('Transferred', godina, mjesec))
	brojTransferred = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = ? AND year = ? AND month = ?", ('Escalated', godina, mjesec))
	brojEscalated = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE status = ? AND year = ? AND month = ?", ('Closed', godina, mjesec))
	brojClosed = c.fetchone()[0]
	conn.commit()
	#BUG - prikazuje 4 active/open tiketa a u bazi imas 5!!!
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (status = ? OR status = ?) AND year = ? AND month = ?", ('Active', 'Open', godina, mjesec))
	brojActive = c.fetchone()[0]
	conn.commit()

	fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

	data = [brojWFC, brojTransferred, brojEscalated, brojClosed, brojActive]
	ingredients = ['WFC', 'Transferred', 'Escalated', 'Closed', 'Active']


	def func(pct, allvals):
		absolute = int(pct/100.*np.sum(allvals))
		return "{:.1f}%\n({:d})".format(pct, absolute)


	wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
		textprops=dict(color="w"))

	ax.legend(wedges, ingredients,
		title="Month / Year\n{0} / {1}".format(mjesec, godina),
		loc="center left",
		bbox_to_anchor=(1, 0, 0.5, 1))

	plt.setp(autotexts, size=8, weight="bold")

	ax.set_title("Status ({0}/{1})".format(mjesec, godina))

	plt.show()
	conn.close()

def SeverityActionAll_triggered():
		conn = sqlite3.connect(bazica)
		c = conn.cursor()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE severity = 'Sev 1'")
		brojSev1 = c.fetchone()[0]
		conn.commit()
		
		c.execute("SELECT COUNT(*) FROM ticket_info WHERE severity = 'Sev 2'")
		brojSev2 = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE severity = 'Sev 3'")
		brojSev3 = c.fetchone()[0]
		conn.commit()

		fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

		data = [brojSev1, brojSev2, brojSev3]
		ingredients = ['Sev 1', 'Sev 2', 'Sev 3']


		def func(pct, allvals):
			absolute = int(pct/100.*np.sum(allvals))
			return "{:.1f}%\n({:d})".format(pct, absolute)


		wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
			textprops=dict(color="w"))

		ax.legend(wedges, ingredients,
			title="Severity (All)",
			loc="center left",
			bbox_to_anchor=(1, 0, 0.5, 1))

		plt.setp(autotexts, size=8, weight="bold")

		ax.set_title("Severity (All)")

		plt.show()
		conn.close()

def SeverityActionYear_triggered(godina):
	conn = sqlite3.connect(bazica)
	c = conn.cursor()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE severity = ? AND year = ?", ('Sev 1', godina))
	brojSev1 = c.fetchone()[0]
	conn.commit()
		
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE severity = ? AND year = ?", ('Sev 2', godina))
	brojSev2 = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE severity = ? AND year = ?", ('Sev 3', godina))
	brojSev3 = c.fetchone()[0]
	conn.commit()

	fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

	data = [brojSev1, brojSev2, brojSev3]
	ingredients = ['Sev 1', 'Sev 2', 'Sev 3']


	def func(pct, allvals):
		absolute = int(pct/100.*np.sum(allvals))
		return "{:.1f}%\n({:d})".format(pct, absolute)

	wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
		textprops=dict(color="w"))

	ax.legend(wedges, ingredients,
		title="Severity (Year {0})".format(godina),
		loc="center left",
		bbox_to_anchor=(1, 0, 0.5, 1))

	plt.setp(autotexts, size=8, weight="bold")

	ax.set_title("Severity (Year {0})".format(godina))

	plt.show()
	conn.close()

def SeverityActionMonth_triggered(godina, mjesec):
	conn = sqlite3.connect(bazica)
	c = conn.cursor()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE severity = ? AND year = ? AND month = ?", ('Sev 1', godina, mjesec))
	brojSev1 = c.fetchone()[0]
	conn.commit()
		
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE severity = ? AND year = ? AND month = ?", ('Sev 2', godina, mjesec))
	brojSev2 = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE severity = ? AND year = ? AND month = ?", ('Sev 3', godina, mjesec))
	brojSev3 = c.fetchone()[0]
	conn.commit()

	fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

	data = [brojSev1, brojSev2, brojSev3]
	ingredients = ['Sev 1', 'Sev 2', 'Sev 3']


	def func(pct, allvals):
		absolute = int(pct/100.*np.sum(allvals))
		return "{:.1f}%\n({:d})".format(pct, absolute)

	wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
		textprops=dict(color="w"))

	ax.legend(wedges, ingredients,
		title="Severity (Year {0})".format(godina),
		loc="center left",
		bbox_to_anchor=(1, 0, 0.5, 1))

	plt.setp(autotexts, size=8, weight="bold")

	ax.set_title("Severity ({0}/{1})".format(mjesec, godina))

	plt.show()
	conn.close()

def CategoryActionAll_triggered():
		conn = sqlite3.connect(bazica)
		c = conn.cursor()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 1")
		brojNetwork = c.fetchone()[0]
		conn.commit()
		
		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 2")
		brojRedundancy = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 3")
		brojEdc = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 4")
		brojInstallation = c.fetchone()[0]
		conn.commit()
		
		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 5")
		brojPrinters = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 6")
		brojReoccurring = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 7")
		brojCashDrawers = c.fetchone()[0]
		conn.commit()
		
		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 8")
		brojEndOfDay = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 9")
		brojAlohaManager = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 10")
		brojHardware = c.fetchone()[0]
		conn.commit()
		
		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 11")
		brojDateTime = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 12")
		brojWindows = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 13")
		brojAlohaTakeOut = c.fetchone()[0]
		conn.commit()
		
		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 14")
		brojLoyalty = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 15")
		brojOrderman = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 16")
		brojDiscrepancy = c.fetchone()[0]
		conn.commit()
		
		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 17")
		brojAlohaKitchen = c.fetchone()[0]
		conn.commit()

		c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = 18")
		brojOther = c.fetchone()[0]
		conn.commit()

		fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

		ingredients = ['Network', 'Redundancy', 'EDC', 'Installation', 'Printers', 'Reoccurring', 'Cash Drawers', 'End Of Day', 'Aloha Manager', 'Hardware', 'Date/Time', 'Windows', 'Aloha Takeout', 'Loyalty', 'Orderman', 'Discrepancy', 'Aloha Kitchen', 'Other']

		data = [brojNetwork, brojRedundancy, brojEdc, brojInstallation, brojPrinters, brojReoccurring, brojCashDrawers, brojEndOfDay, brojAlohaManager, brojHardware, brojDateTime, brojWindows, brojAlohaTakeOut, brojLoyalty, brojOrderman, brojDiscrepancy, brojAlohaKitchen, brojOther]

		wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

		bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
		kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
		          bbox=bbox_props, zorder=0, va="center")

		for i, p in enumerate(wedges):
			ang = (p.theta2 - p.theta1)/2. + p.theta1
			y = np.sin(np.deg2rad(ang))
			x = np.cos(np.deg2rad(ang))
			horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
			connectionstyle = "angle,angleA=0,angleB={}".format(ang)
			kw["arrowprops"].update({"connectionstyle": connectionstyle})
			ax.annotate('{0} ({1})'.format(ingredients[i], data[i]), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
				horizontalalignment=horizontalalignment, **kw)

		plt.show()
		conn.close()

def CategoryActionYear_triggered(godina):
	conn = sqlite3.connect(bazica)
	c = conn.cursor()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (1, godina))
	brojNetwork = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (2, godina))
	brojRedundancy = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (3, godina))
	brojEdc = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (4, godina))
	brojInstallation = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (5, godina))
	brojPrinters = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (6, godina))
	brojReoccurring = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (7, godina))
	brojCashDrawers = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (8, godina))
	brojEndOfDay = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (9, godina))
	brojAlohaManager = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (10, godina))
	brojHardware = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (11, godina))
	brojDateTime = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (12, godina))
	brojWindows = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (13, godina))
	brojAlohaTakeOut = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (14, godina))
	brojLoyalty = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (15, godina))
	brojOrderman = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (16, godina))
	brojDiscrepancy = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (17, godina))
	brojAlohaKitchen = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ?", (18, godina))
	brojOther = c.fetchone()[0]
	conn.commit()

	fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

	ingredients = ['Network', 'Redundancy', 'EDC', 'Installation', 'Printers', 'Reoccurring', 'Cash Drawers', 'End Of Day', 'Aloha Manager', 'Hardware', 'Date/Time', 'Windows', 'Aloha Takeout', 'Loyalty', 'Orderman', 'Discrepancy', 'Aloha Kitchen', 'Other']

	data = [brojNetwork, brojRedundancy, brojEdc, brojInstallation, brojPrinters, brojReoccurring, brojCashDrawers, brojEndOfDay, brojAlohaManager, brojHardware, brojDateTime, brojWindows, brojAlohaTakeOut, brojLoyalty, brojOrderman, brojDiscrepancy, brojAlohaKitchen, brojOther]

	wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

	bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
	kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
		bbox=bbox_props, zorder=0, va="center")

	for i, p in enumerate(wedges):
		ang = (p.theta2 - p.theta1)/2. + p.theta1
		y = np.sin(np.deg2rad(ang))
		x = np.cos(np.deg2rad(ang))
		horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
		connectionstyle = "angle,angleA=0,angleB={}".format(ang)
		kw["arrowprops"].update({"connectionstyle": connectionstyle})
		ax.annotate('{0} ({1})'.format(ingredients[i], data[i]), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
			horizontalalignment=horizontalalignment, **kw)

	plt.show()
	conn.close()

def CategoryActionMonth_triggered(godina, mjesec):
	conn = sqlite3.connect(bazica)
	c = conn.cursor()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (1, godina, mjesec))
	brojNetwork = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (2, godina, mjesec))
	brojRedundancy = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (3, godina, mjesec))
	brojEdc = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (4, godina, mjesec))
	brojInstallation = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (5, godina, mjesec))
	brojPrinters = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (6, godina, mjesec))
	brojReoccurring = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (7, godina, mjesec))
	brojCashDrawers = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (8, godina, mjesec))
	brojEndOfDay = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (9, godina, mjesec))
	brojAlohaManager = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (10, godina, mjesec))
	brojHardware = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (11, godina, mjesec))
	brojDateTime = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (12, godina, mjesec))
	brojWindows = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (13, godina, mjesec))
	brojAlohaTakeOut = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (14, godina, mjesec))
	brojLoyalty = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (15, godina, mjesec))
	brojOrderman = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (16, godina, mjesec))
	brojDiscrepancy = c.fetchone()[0]
	conn.commit()
	
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (17, godina, mjesec))
	brojAlohaKitchen = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE kategorija = ? AND year = ? AND month = ?", (18, godina, mjesec))
	brojOther = c.fetchone()[0]
	conn.commit()

	fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

	ingredients = ['Network', 'Redundancy', 'EDC', 'Installation', 'Printers', 'Reoccurring', 'Cash Drawers', 'End Of Day', 'Aloha Manager', 'Hardware', 'Date/Time', 'Windows', 'Aloha Takeout', 'Loyalty', 'Orderman', 'Discrepancy', 'Aloha Kitchen', 'Other']

	data = [brojNetwork, brojRedundancy, brojEdc, brojInstallation, brojPrinters, brojReoccurring, brojCashDrawers, brojEndOfDay, brojAlohaManager, brojHardware, brojDateTime, brojWindows, brojAlohaTakeOut, brojLoyalty, brojOrderman, brojDiscrepancy, brojAlohaKitchen, brojOther]

	wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

	bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
	kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
		bbox=bbox_props, zorder=0, va="center")

	for i, p in enumerate(wedges):
		ang = (p.theta2 - p.theta1)/2. + p.theta1
		y = np.sin(np.deg2rad(ang))
		x = np.cos(np.deg2rad(ang))
		horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
		connectionstyle = "angle,angleA=0,angleB={}".format(ang)
		kw["arrowprops"].update({"connectionstyle": connectionstyle})
		ax.annotate('{0} ({1})'.format(ingredients[i], data[i]), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
			horizontalalignment=horizontalalignment, **kw)

	plt.show()
	conn.close()

def DurationActionAll_triggered():
	conn = sqlite3.connect(bazica)
	c = conn.cursor()

	# 0-15min,  15min-45min, 45min-1h, 1h-1h30min, 1h30min-2h, 2h-
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE vrijeme_trajanja_poziva_m < 15 AND vrijeme_trajanja_poziva_h = 0")
	brojDo15 = c.fetchone()[0]
	conn.commit()
		
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE vrijeme_trajanja_poziva_m < 45 AND vrijeme_trajanja_poziva_m >= 15 AND vrijeme_trajanja_poziva_h = 0")
	brojDo45 = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE vrijeme_trajanja_poziva_m >= 45 AND vrijeme_trajanja_poziva_m <= 59 AND vrijeme_trajanja_poziva_h = 0")
	brojDoSat = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE vrijeme_trajanja_poziva_m >= 0 AND vrijeme_trajanja_poziva_m <= 30 AND vrijeme_trajanja_poziva_h = 1")
	brojDoSatipo = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE vrijeme_trajanja_poziva_m >= 30 AND vrijeme_trajanja_poziva_m <= 59 AND vrijeme_trajanja_poziva_h = 1")
	brojDo2Sata = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE vrijeme_trajanja_poziva_h >= 2")
	preko2Sata = c.fetchone()[0]
	conn.commit()

	fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

	data = [brojDo15, brojDo45, brojDoSat, brojDoSatipo, brojDo2Sata, preko2Sata]
	ingredients = ['0 - 15min', '15 - 45min', '45min - 1h', '1h - 1h30min', '1h30min - 2h', '2h - ']


	def func(pct, allvals):
		absolute = int(pct/100.*np.sum(allvals))
		return "{:.1f}%".format(pct, absolute)


	wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
		textprops=dict(color="w"))

	ax.legend(wedges, ingredients,
		title="Call Duration (All)",
		loc="center left",
		bbox_to_anchor=(1, 0, 0.5, 1))

	plt.setp(autotexts, size=8, weight="bold")

	ax.set_title("Call Duration (All)")

	plt.show()

	conn.close()

def DurationActionYear_triggered(godina):
	conn = sqlite3.connect(bazica)
	c = conn.cursor()

	# 0-15min,  15min-45min, 45min-1h, 1h-1h30min, 1h30min-2h, 2h-
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m < ? AND vrijeme_trajanja_poziva_h = ?) AND year = ?", (15, 0, godina))
	brojDo15 = c.fetchone()[0]
	conn.commit()
		
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m < ? AND vrijeme_trajanja_poziva_m >= ? AND vrijeme_trajanja_poziva_h = ?) AND year = ?", (45, 15, 0, godina))
	brojDo45 = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m >= ? AND vrijeme_trajanja_poziva_m <= ? AND vrijeme_trajanja_poziva_h = ?) AND year = ?", (45, 59, 0, godina))
	brojDoSat = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m >= ? AND vrijeme_trajanja_poziva_m <= ? AND vrijeme_trajanja_poziva_h = ?) AND year = ?", (0, 30, 1, godina))
	brojDoSatipo = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m >= ? AND vrijeme_trajanja_poziva_m <= ? AND vrijeme_trajanja_poziva_h = ?) AND year = ?", (30, 59, 1, godina))
	brojDo2Sata = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE vrijeme_trajanja_poziva_h >= ? AND year = ?", (2, godina))
	preko2Sata = c.fetchone()[0]
	conn.commit()

	fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

	data = [brojDo15, brojDo45, brojDoSat, brojDoSatipo, brojDo2Sata, preko2Sata]
	ingredients = ['0 - 15min', '15 - 45min', '45min - 1h', '1h - 1h30min', '1h30min - 2h', '2h - ']


	def func(pct, allvals):
		absolute = int(pct/100.*np.sum(allvals))
		return "{:.1f}%".format(pct, absolute)


	wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
		textprops=dict(color="w"))

	ax.legend(wedges, ingredients,
		title="Call Duration (Year {0})".format(godina),
		loc="center left",
		bbox_to_anchor=(1, 0, 0.5, 1))

	plt.setp(autotexts, size=8, weight="bold")

	ax.set_title("Call Duration (Year {0})".format(godina))

	plt.show()

	conn.close()

def DurationActionMonth_triggered(godina, mjesec):
	conn = sqlite3.connect(bazica)
	c = conn.cursor()

	# 0-15min,  15min-45min, 45min-1h, 1h-1h30min, 1h30min-2h, 2h-
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m < ? AND vrijeme_trajanja_poziva_h = ?) AND (year = ? AND month = ?)", (15, 0, godina, mjesec))
	brojDo15 = c.fetchone()[0]
	conn.commit()
		
	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m < ? AND vrijeme_trajanja_poziva_m >= ? AND vrijeme_trajanja_poziva_h = ?) AND (year = ? AND month = ?)", (45, 15, 0, godina, mjesec))
	brojDo45 = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m >= ? AND vrijeme_trajanja_poziva_m <= ? AND vrijeme_trajanja_poziva_h = ?) AND (year = ? AND month = ?)", (45, 59, 0, godina, mjesec))
	brojDoSat = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m >= ? AND vrijeme_trajanja_poziva_m <= ? AND vrijeme_trajanja_poziva_h = ?) AND (year = ? AND month = ?)", (0, 30, 1, godina, mjesec))
	brojDoSatipo = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE (vrijeme_trajanja_poziva_m >= ? AND vrijeme_trajanja_poziva_m <= ? AND vrijeme_trajanja_poziva_h = ?) AND (year = ? AND month = ?)", (30, 59, 1, godina, mjesec))
	brojDo2Sata = c.fetchone()[0]
	conn.commit()

	c.execute("SELECT COUNT(*) FROM ticket_info WHERE vrijeme_trajanja_poziva_h >= ? AND year = ? AND month = ?", (2, godina, mjesec))
	preko2Sata = c.fetchone()[0]
	conn.commit()

	fig, ax = plt.subplots(figsize=(10, 6), subplot_kw=dict(aspect="equal"))

	data = [brojDo15, brojDo45, brojDoSat, brojDoSatipo, brojDo2Sata, preko2Sata]
	ingredients = ['0 - 15min', '15 - 45min', '45min - 1h', '1h - 1h30min', '1h30min - 2h', '2h - ']


	def func(pct, allvals):
		absolute = int(pct/100.*np.sum(allvals))
		return "{:.1f}%".format(pct, absolute)


	wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
		textprops=dict(color="w"))

	ax.legend(wedges, ingredients,
		title="Call Duration ({0}/{1})".format(mjesec, godina),
		loc="center left",
		bbox_to_anchor=(1, 0, 0.5, 1))

	plt.setp(autotexts, size=8, weight="bold")

	ax.set_title("Call Duration (Year {0})".format(godina))

	plt.show()

	conn.close()