"""
NOOBNOTE : PRONOTE en moins bien
Fichier : app.py
Auteur : Kilian PEYRON
"""
import sqlite3 as sql
import datetime

connexion = sql.connect('noobnote', isolation_level=None)
base = connexion.cursor()

def cDevoir(dbdate, coeff):
	base.execute('INSERT INTO controles (matiere, date_controle, coeff) VALUES(?, ?, ?)',('MATHEMATIQUES',dbdate,coeff))
	print("Done.")

def sControle(idcontrole):
	base.execute("DELETE FROM controles WHERE idcontrole = ?", idcontrole)
	base.execute("DELETE FROM notes WHERE idcontrole = ?", idcontrole)
	print("Done.")

def ajNote(idcontrole, p):
	notes = {}
	base.execute('SELECT COUNT(*) FROM eleves')
	data_elv = base.fetchone()
	for i in range(1, data_elv[0]+1):
		notes['note_eleve'+str(i)] = p['ne'+str(i)]
	print(notes)
	base.execute("SELECT COUNT(*) FROM notes WHERE idcontrole = ?", idcontrole)
	data = base.fetchone()
	ntsExist = data[0]
	# Si des notes ont déja été rentrées
	if(ntsExist >= 1):
		elvs = 1
		for i in range(len(notes)):
			base.execute('UPDATE notes SET note = ? WHERE uid = ? AND idcontrole = ?', (notes['note_eleve'+str(elvs)], str(elvs), idcontrole))
			print("Note : " + notes['note_eleve'+str(elvs)], "idEleve : " + str(elvs), "idControle : " + idcontrole)
			elvs += 1
		print('Done.')
	else:
		elvs = 1
		for i in range(len(notes)):
			base.execute('INSERT INTO notes (uid, note, idcontrole) VALUES (?, ?, ?)', (str(elvs), notes['note_eleve'+str(elvs)], idcontrole))
			print("Note : " + notes['note_eleve'+str(elvs)], "idEleve : " + str(elvs), "idControle : " + idcontrole)
			elvs += 1
		print('Done.')

def verifBouton(idcontrole):
	# Vérifications
	base.execute("SELECT COUNT(*) FROM notes WHERE idcontrole = ?", idcontrole)
	data = base.fetchone()
	ntsExist = data[0]
	# Si des notes ont déja été rentrées
	return ntsExist >= 1

def rcpEleves():
	base.execute('SELECT * FROM eleves')
	data = base.fetchall()
	donnee = []
	for eleves in data:
		# Moyenne
		base.execute('SELECT SUM(note) FROM notes WHERE uid = ?', str(eleves[0]))
		moy = base.fetchone()
		# Nombre de notes
		base.execute('SELECT COUNT(*) FROM notes WHERE uid = ?', str(eleves[0]));
		nb_notes = base.fetchone()
		nb_nts = nb_notes[0]
		# Moyenne finale
		moyenne = int(moy[0]) / nb_nts
		# Affichage
		donnee.append([eleves[1],eleves[2], str(eleves[0]), str(moyenne)])
	return donnee

def rcpControles():
	base.execute('SELECT * FROM controles')
	data_controles = base.fetchall()
	donnee = []
	for controles in data_controles:
		donnee.append([str(controles[0]), controles[1], controles[2], controles[3]])
	return donnee
	
def rcpProfs():
	base.execute('SELECT * FROM professeur')
	data_profs = base.fetchall()
	donnee = []
	for profs in data_profs:
		donnee.append([str(profs[0]), str(profs[1])])
	return donnee

def rcpNotes():
	base.execute('SELECT * FROM notes JOIN eleves USING(uid) ORDER BY idcontrole DESC LIMIT 10')
	data_notes = base.fetchall()
	donnee = []
	for notes in data_notes:
		donnee.append([str(notes[1]), str(notes[4]), str(notes[5]), str(notes[2]), str(notes[3])])
	return donnee
	
def nbProfs():
	base.execute('SELECT COUNT(*) FROM professeur');
	nb_profs = base.fetchone()
	nb_prfs = str(nb_profs[0])
	return nb_prfs
	
def nbEleves():
	base.execute('SELECT COUNT(*) FROM eleves');
	nb_eleves = base.fetchone()
	nb = str(nb_eleves[0])
	return nb

def nbControles():
	base.execute('SELECT COUNT(*) FROM controles');
	nb_controles = base.fetchone()
	nb_ctl = str(nb_controles[0])
	return nb_ctl

