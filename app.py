"""
NOOBNOTE : PRONOTE en moins bien
Fichier : app.py
Auteur : Kilian PEYRON
"""
from fonctions import *
import htinter
import datetime


date = datetime.datetime.now()
dbdate = (date.strftime("%Y-%m-%d %H:%M"))


def creerDevoir(c,p):
	coeff = p['val']
	cDevoir(dbdate, coeff)
	htinter.charge_page('index.html')

def supprimerControle(c,p):
	idcontrole = p['ctl_id']
	sControle(idcontrole)
	htinter.charge_page('index.html')
 
def ajouterNote(c,p):
	idcontrole = p['ctl_id']
	ajNote(idcontrole, p)
	htinter.charge_page('index.html')
	
	
def lierParam():
	for i in range(1, int(nbEleves())+1):
		htinter.lier_param("note_eleve"+str(i), "ne"+str(i))
		
def afficherInput(c,p):
	for i in range(1, int(nbEleves())+1):
		htinter.classes("note_eleve"+str(i),"dblock")

	htinter.classes("ajouter_notes","btn-devoir dblock")
	
	lierParam()

	idcontrole = p['ctl_id']
	verifBouton(idcontrole)
	
	if verifBouton(idcontrole):
		htinter.contenu("ajouter_notes","Mettre à jour")
	else:
		htinter.contenu("ajouter_notes","Valider les notes")

def fonction_d_initialisation( c, p ):
	htinter.capture_clic("nnModalBtnSubmit", fnct=creerDevoir)
	htinter.lier_param("nnModalCoeff", "val")
	
	for donnee in rcpEleves():
		htinter.contenu("eleves", "<tr><td>"+ donnee[0] + ' ' + donnee[1] +"</td><td><input type='number' max='20' min='0' id='note_eleve"+ donnee[2] +"'></td><td>"+ donnee[3] +"</td></tr>", True)

	for donnee in rcpControles():
		htinter.contenu("controles", "<tr><td>"+ donnee[0] +"</td><td style='text-transform:uppercase;'>"+ donnee[1] + "</td><td>"+ donnee[2] +"</td><td>"+ donnee[3] +"</td></tr>", True)
		htinter.contenu("slct_controle", "<option value='"+ donnee[0] +"' id='slct_controle' style='text-transform:uppercase;'>ID: "+ donnee[0] + " - " + donnee[1] +"</option>", True)

	for donnee in rcpProfs():
		htinter.contenu("profs", "<tr><td>"+ donnee[0] +"</td><td style='text-transform:uppercase;'>"+ donnee[1] + "</td></tr>", True)

	for donnee in rcpNotes():
		htinter.contenu("notes", "<tr><td>"+ donnee[0] +"</td><td>"+ donnee[1] + " " + donnee[2] +"</td><td>"+ donnee[3] +"</td><td>"+ donnee[4] +"</td></tr>", True)


	htinter.contenu("nb_profs", "Profésseurs ("+ nbProfs() +")")
	htinter.contenu("nb_eleves", "("+ nbEleves() +") élèves")
	htinter.contenu("nb_controles", "Mes Devoirs ("+ nbControles() +")")
	htinter.capture_clic("saisir_notes",fnct=afficherInput)
	htinter.lier_param("slct_controle", "ctl_id")
	htinter.capture_clic("ajouter_notes", fnct=ajouterNote)
	htinter.capture_clic("supprimer_devoir", fnct=supprimerControle)

	

htinter.init_page( fonction_d_initialisation )
htinter.servir()
