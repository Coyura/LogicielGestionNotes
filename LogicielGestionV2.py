import sys, json
from itertools import chain
from PySide2.QtWidgets import (QLabel, QApplication, QDoubleSpinBox, QTableWidgetItem, QLineEdit, QMessageBox, QGroupBox, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy,QMainWindow)
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
import pandas as pd
import numpy as np
from math import pi
import matplotlib.pyplot as plt
from ui_designLogicielFinalV5 import Ui_MainWindow

filename = "dataNotesV2.json"

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global filename
        self.mesDatas = {}

        self.mesDatas = self.lireJSON(filename)

        #Hide and show the differents windows:
        self.ui.gBMoyBulletin.hide()
        self.ui.gBAjoutAcad.hide()
        self.ui.gBAjoutEtab.hide()
        self.ui.gBAjoutClasse.hide()
        self.ui.gBAjoutEleve.hide()
        self.ui.gBAjoutMat.hide()
        self.ui.gBModifierNotes.hide()
        self.ui.pBGestNote.clicked.connect(self.showGestionNotes)
        self.ui.pBMoyenne.clicked.connect(self.showBulletin)
        self.ui.pBAjoutAcademie.clicked.connect(self.showAjoutAcad)
        self.ui.pBAjoutEtablissement.clicked.connect(self.showAjoutEtab)
        self.ui.pBAjoutClasse.clicked.connect(self.showAjoutClasse)
        self.ui.pBAjoutEleve.clicked.connect(self.showAjoutEleve)
        self.ui.pBAjoutMatiere.clicked.connect(self.showAjoutMat)
        self.ui.pBModifNotes.clicked.connect(self.showModifNote)


        # Il faut maintenant charger les établissements de l'académie choisie :
        self.ui.cBAcademie.currentIndexChanged.connect(self.updateEtablissement)

        # Il faut maintenant charger les classes de l'établissement choisie :
        self.ui.cBEtablissement.currentIndexChanged.connect(self.updateClasse)

        self.ui.cBClasse.currentIndexChanged.connect(self.updateMatiere)
        self.ui.cBMatiereGBNote.currentIndexChanged.connect(self.updateSaisieEleve)
        self.ui.cBMatiereModifNote.currentIndexChanged.connect(self.updateDevoir)
        self.ui.pBAffNote.clicked.connect(self.affichNote)
        self.ui.pBValiderModifNote.clicked.connect(self.modifNote)

        # Ajout d'un nouveau Devoir/Note:
        self.ui.pBValiderNotation.clicked.connect(self.ajoutNote)

        # Ajout d'une nouvelle Académie
        self.ui.pBValNewAcad.clicked.connect(self.ajoutAcademie)

        # Ajout Nouvel Etablissement
        self.ui.pBValNewEtab.clicked.connect(self.ajoutEtablissement)

        # Ajout Nouvelle Classe
        self.ui.cBListAcadClass.currentIndexChanged.connect(self.updateEtabAjoutClasse)
        self.ui.pBValNewClass.clicked.connect(self.ajoutClasse)

        # Ajout Nouvel Eleve
        self.ui.cBListAcadEleve.currentIndexChanged.connect(self.updateEtabAjoutEleve)
        self.ui.cBListEtabEleve.currentIndexChanged.connect(self.updateClasseEleve)
        self.ui.pBValNewEleve.clicked.connect(self.ajoutEleve)

        # Ajout Matière
        self.ui.cBAcadMat.currentIndexChanged.connect(self.updateEtabAjoutMat)
        self.ui.cBEtabMat.currentIndexChanged.connect(self.updateClassAjoutMat)
        self.ui.cBClassMat.currentIndexChanged.connect(self.updateElevAjoutMat)
        self.ui.pBValMat.clicked.connect(self.ajoutMatière)

        # Modif données Etab, Classe, Eleves, Matiere


        # Calcul Moyennes Eleve
        self.ui.pBValAppr.clicked.connect(self.updateApprecia)
        # self.ui.pBValCalculMoy.clicked.connect(self.calculMoyenne)
        self.ui.pBValCalculMoy.clicked.connect(self.affichageMoyEleCla)


        # Il faut charger les académies dans la comboBox:
        self.updateAcademie()

        # Chargement de la liste des élèves d'une matière pour bulletin
        self.ui.cBClasse.currentIndexChanged.connect(self.updateEleveBulletin)



    def showGestionNotes(self):
        self.ui.gBGestionNotes.setVisible(True)
        self.ui.gBMoyBulletin.hide()
        self.ui.gBAjoutAcad.hide()
        self.ui.gBAjoutEtab.hide()
        self.ui.gBAjoutClasse.hide()
        self.ui.gBAjoutEleve.hide()
        self.ui.gBAjoutMat.hide()
        self.ui.gBModifierNotes.hide()

    def showModifNote(self):
        self.ui.gBModifierNotes.setVisible(True)
        self.ui.gBGestionNotes.hide()
        self.ui.gBMoyBulletin.hide()
        self.ui.gBAjoutAcad.hide()
        self.ui.gBAjoutEtab.hide()
        self.ui.gBAjoutClasse.hide()
        self.ui.gBAjoutEleve.hide()
        self.ui.gBAjoutMat.hide()

    def showBulletin(self):
        self.ui.gBMoyBulletin.setVisible(True)
        self.ui.gBGestionNotes.hide()
        self.ui.gBAjoutAcad.hide()
        self.ui.gBAjoutEtab.hide()
        self.ui.gBAjoutClasse.hide()
        self.ui.gBAjoutEleve.hide()
        self.ui.gBAjoutMat.hide()
        self.ui.gBModifierNotes.hide()
        self.updateEleveBulletin()

    def showAjoutAcad(self):
        self.ui.gBAjoutAcad.setVisible(True)
        self.ui.gBGestionNotes.hide()
        self.ui.gBMoyBulletin.hide()
        self.ui.gBAjoutEtab.hide()
        self.ui.gBAjoutClasse.hide()
        self.ui.gBAjoutEleve.hide()
        self.ui.gBAjoutMat.hide()
        self.ui.gBModifierNotes.hide()

    def showAjoutEtab(self):
        self.ui.gBAjoutEtab.setVisible(True)
        self.ui.gBGestionNotes.hide()
        self.ui.gBMoyBulletin.hide()
        self.ui.gBAjoutAcad.hide()
        self.ui.gBAjoutClasse.hide()
        self.ui.gBAjoutEleve.hide()
        self.ui.gBAjoutMat.hide()
        self.ui.gBModifierNotes.hide()

    def showAjoutClasse(self):
        self.ui.gBAjoutClasse.setVisible(True)
        self.ui.gBGestionNotes.hide()
        self.ui.gBMoyBulletin.hide()
        self.ui.gBAjoutAcad.hide()
        self.ui.gBAjoutEtab.hide()
        self.ui.gBAjoutEleve.hide()
        self.ui.gBAjoutMat.hide()
        self.ui.gBModifierNotes.hide()

    def showAjoutEleve(self):
        self.ui.gBAjoutEleve.setVisible(True)
        self.ui.gBGestionNotes.hide()
        self.ui.gBMoyBulletin.hide()
        self.ui.gBAjoutAcad.hide()
        self.ui.gBAjoutEtab.hide()
        self.ui.gBAjoutClasse.hide()
        self.ui.gBAjoutMat.hide()
        self.ui.gBModifierNotes.hide()

    def showAjoutMat(self):
        self.ui.gBAjoutMat.setVisible(True)
        self.ui.gBGestionNotes.hide()
        self.ui.gBMoyBulletin.hide()
        self.ui.gBAjoutAcad.hide()
        self.ui.gBAjoutEtab.hide()
        self.ui.gBAjoutClasse.hide()
        self.ui.gBAjoutEleve.hide()
        self.ui.gBModifierNotes.hide()

    def updateAcademie (self):
        for acad in self.mesDatas["academies"]:
            self.ui.cBAcademie.addItem(acad["nom"])
            self.ui.cBListAcad.addItem(acad["nom"])
            self.ui.cBListAcadClass.addItem(acad["nom"])
            self.ui.cBListAcadEleve.addItem(acad["nom"])
            self.ui.cBAcadMat.addItem(acad["nom"])
            print(acad["nom"])

    def updateEtablissement(self):
        print("prout")
        self.ui.cBEtablissement.clear()
        # self.ui.cBListEtabClass.clear()
        # self.ui.cBListEtabEleve.clear()
        academie = self.ui.cBAcademie.currentIndex()
        for etab in self.mesDatas["academies"][academie]["etablissements"]:
            self.ui.cBEtablissement.addItem(etab["nom"])
            # self.ui.cBListEtabClass.addItem(etab["nom"])
            # self.ui.cBListEtabEleve.addItem(etab["nom"])
            print(etab["nom"])

    def updateClasse(self):
        self.ui.cBClasse.clear()
        ## self.ui.cBClasseGPNote.clear()
        ## self.ui.cBClasseGPNote.clear()
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        for cla in self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"]:
            self.ui.cBClasse.addItem(cla["nom"])
            ## self.ui.cBClasseGPNote.addItem(cla["nom"])

    def updateMatiere (self) :
        self.ui.cBMatiereGBNote.clear()
        self.ui.cBMatiereModifNote.clear()
        ## self.ui.cBMatiereBulletin.clear()
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        listeMatieres = []
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        for eleve in dicoClasse["eleves"]:
            for matiere in eleve["matieres"]:
                listeMatieres.append(matiere["nom"])
        listeMatieresUniques = np.unique(listeMatieres)
        self.ui.cBMatiereGBNote.addItems(listeMatieresUniques)
        self.ui.cBMatiereModifNote.addItems(listeMatieresUniques)

    def ajoutAcademie (self):
        print("Ajout Académie")
        fiche = {}
        fiche["nom"]= self.ui.lENomAcad.text()
        fiche["etablissements"]=[]
        if self.ui.lENomAcad.text()=='':
            msgErreur = QMessageBox()
            msgErreur.setWindowTitle("Erreur")
            msgErreur.setText("Le nom de l'académie est manquant")
            msgErreur.exec()
        else:
            self.mesDatas["academies"].append(fiche)
            self.sauveJSON(filename)
            print(fiche)
            self.ui.cBAcademie.addItem(fiche["nom"])
            self.ui.cBListAcad.addItem(fiche["nom"])
            self.ui.cBListAcadClass.addItem(fiche["nom"])
            self.ui.cBListAcadEleve.addItem(fiche["nom"])
            self.ui.cBAcadMat.addItem(fiche["nom"])

    def ajoutEtablissement(self):
        print("Ajout Etablissement")
        ficheE = {}
        academie = self.ui.cBListAcad.currentIndex()
        dicoEtab=self.mesDatas["academies"][academie]["etablissements"]
        ficheE["nom"]=self.ui.lENomEtab.text()
        ficheE["adresse"]=self.ui.lEEtabAdress.text()
        ficheE["classes"]=[]
        if self.ui.lENomEtab.text()=='':
            msgErreur = QMessageBox()
            msgErreur.setWindowTitle("Erreur")
            msgErreur.setText("Le nom de l'établissement est manquant")
            msgErreur.exec()
        elif self.ui.lEEtabAdress.text()=='':
            msgErreurAd = QMessageBox()
            msgErreurAd.setWindowTitle("Erreur")
            msgErreurAd.setText("L'adresse de l'établissement est manquante")
            msgErreurAd.exec()
        else:
            dicoEtab.append(ficheE)
            self.sauveJSON(filename)
            print(ficheE)
        self.ui.cBEtablissement.addItem(ficheE["nom"])
        # self.ui.cBListEtabClass.addItem(ficheE["nom"])
        # self.ui.cBListEtabEleve.addItem(ficheE["nom" ])

    def ajoutClasse(self):
        print("Ajout Classe")
        ficheC = {}
        academie = self.ui.cBListAcadClass.currentIndex()
        etab = self.ui.cBListEtabClass.currentIndex()
        dicoClasse=self.mesDatas["academies"][academie]["etablissements"][etab]["classes"]
        ficheC["nom"]=self.ui.lENomClasse.text()
        ficheC["anneeSco"]=self.ui.lEAnneScol.text()
        ficheC["PP"]=self.ui.lEProfPrinc.text()
        ficheC["eleves"]=[]
        if self.ui.lENomClasse.text()=='':
            msgErreur = QMessageBox()
            msgErreur.setWindowTitle("Erreur")
            msgErreur.setText("Le nom de la classe est manquant")
            msgErreur.exec()
        elif self.ui.lEAnneScol.text()=='':
            msgErreurAd = QMessageBox()
            msgErreurAd.setWindowTitle("Erreur")
            msgErreurAd.setText("L'année scolaire est manquante")
            msgErreurAd.exec()
        elif self.ui.lEProfPrinc.text()=='':
            msgErreurAd = QMessageBox()
            msgErreurAd.setWindowTitle("Erreur")
            msgErreurAd.setText("Le nom du professeur principal est manquant")
            msgErreurAd.exec()
        else:
            dicoClasse.append(ficheC)
            self.sauveJSON(filename)
            print(ficheC)

    def updateEtabAjoutClasse (self):
        self.ui.cBListEtabClass.clear()
        academie = self.ui.cBListAcadClass.currentIndex()
        for etab in self.mesDatas["academies"][academie]["etablissements"]:
            self.ui.cBListEtabClass.addItem(etab["nom"])

    def ajoutEleve(self):
        print("Ajout Elève")
        ficheE = {}
        academie = self.ui.cBListAcad.currentIndex()
        etab=self.ui.cBListEtabEleve.currentIndex()
        cla=self.ui.cBListClassEleve.currentIndex()
        dicoEleve=self.mesDatas["academies"][academie]["etablissements"][etab]["classes"][cla]["eleves"]
        ficheE["nom"]=self.ui.lENomEleve.text()
        ficheE["prenom"]=self.ui.lEPrenomEleve.text()
        ficheE["adresse"]=""
        ficheE["appreciationPP"]=""
        ficheE["matieres"]=[]
        if self.ui.lENomEleve.text()=='':
            msgErreur = QMessageBox()
            msgErreur.setWindowTitle("Erreur")
            msgErreur.setText("Le nom de l'élève est manquant")
            msgErreur.exec()
        elif self.ui.lEPrenomEleve.text()=='':
            msgErreurAd = QMessageBox()
            msgErreurAd.setWindowTitle("Erreur")
            msgErreurAd.setText("Le prénom de l'élève est manquant")
            msgErreurAd.exec()
        elif self.ui.lEAdresseElev.text()=='':
            msgErreurAd = QMessageBox()
            msgErreurAd.setWindowTitle("Erreur")
            msgErreurAd.setText("L'adresse de l'élève est manquante")
            msgErreurAd.exec()
        else:
            dicoEleve.append(ficheE)
            self.sauveJSON(filename)
            print(ficheE)

    def updateEtabAjoutEleve (self):
        self.ui.cBListEtabEleve.clear()
        academie = self.ui.cBListAcadEleve.currentIndex()
        for etab in self.mesDatas["academies"][academie]["etablissements"]:
            self.ui.cBListEtabEleve.addItem(etab["nom"])

    def updateClasseEleve(self):
        self.ui.cBListClassEleve.clear()
        academie = self.ui.cBListAcadEleve.currentIndex()
        etab = self.ui.cBListEtabEleve.currentIndex()
        for cla in self.mesDatas["academies"][academie]["etablissements"][etab]["classes"]:
            self.ui.cBListClassEleve.addItem(cla["nom"])

    def ajoutMatière(self):
        print("Ajout Matière")
        ficheM = {}
        academie = self.ui.cBAcadMat.currentIndex()
        etab = self.ui.cBEtabMat.currentIndex()
        cla = self.ui.cBClassMat.currentIndex()
        elev = self.ui.cBElevMat.currentIndex()
        dicoMat = self.mesDatas["academies"][academie]["etablissements"][etab]["classes"][cla]["eleves"][elev]["matieres"]
        ficheM["nom"] = self.ui.lENomMat.text()
        ficheM["coef"] = self.ui.dSBCoeffMat.value()
        ficheM["appreciation"] = ""
        # ficheM["notes"] = [{"nom":str(),"coef":float(),"valeur":float()}]
        ficheM["notes"]=[]
        dicoMat.append(ficheM)
        self.sauveJSON(filename)
        print(ficheM)

    def updateDevoir(self):
        self.ui.cBListeDevoir.clear()
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        matNom=self.ui.cBMatiereModifNote.currentText()
        # mat=self.ui.cBMatiereModifNote.currentIndex()
        listeDevoir = []
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        for eleve in dicoClasse["eleves"]:
            # dicoMat=eleve["matieres"][mat]
            for matiere in eleve["matieres"]:
                if matiere["nom"]==matNom :
                    dicoDevoir=matiere["notes"]
                    for devoir in dicoDevoir:
                        listeDevoir.append(devoir["nom"])
        listeDevoirUniques = np.unique(listeDevoir)
        self.ui.cBListeDevoir.addItems(listeDevoirUniques)

    def updateEtabAjoutMat(self):
        academie = self.ui.cBAcadMat.currentIndex()
        for etab in self.mesDatas["academies"][academie]["etablissements"]:
            self.ui.cBEtabMat.addItem(etab["nom"])

    def updateClassAjoutMat(self):
        self.ui.cBClassMat.clear()
        academie = self.ui.cBAcadMat.currentIndex()
        etab = self.ui.cBEtabMat.currentIndex()
        for cla in self.mesDatas["academies"][academie]["etablissements"][etab]["classes"]:
            self.ui.cBClassMat.addItem(cla["nom"])

    def updateElevAjoutMat(self):
        self.ui.cBElevMat.clear()
        academie = self.ui.cBAcadMat.currentIndex()
        etab = self.ui.cBEtabMat.currentIndex()
        cla = self.ui.cBClassMat.currentIndex()
        for elev in self.mesDatas["academies"][academie]["etablissements"][etab]["classes"][cla]["eleves"]:
            self.ui.cBElevMat.addItem(elev["nom"])

    def updateSaisieEleve(self):
        cpt=0
        self.ui.tWTableNotation.clear()
        self.ui.tWTableNotation.setColumnCount(3)
        # ça permettait de définir le nombre de colonne de la tableWidget si non défini dans le QtDesigner
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        for eleve in dicoClasse["eleves"]:
            for matiere in eleve["matieres"]:
                mat=self.ui.cBMatiereGBNote.currentText()
                if matiere["nom"]==mat:
                    nomE = eleve["nom"]
                    prenomE = eleve["prenom"]
                    self.ui.tWTableNotation.setRowCount(cpt+1)
                    itemE=QTableWidgetItem(nomE)
                    itemPE=QTableWidgetItem(prenomE)
                    self.ui.tWTableNotation.setItem(cpt,0,itemE)
                    self.ui.tWTableNotation.setItem(cpt,1, itemPE)
                    # utiliser le QDoubleSpin permet de rentrer une note en transformant direct en float
                    spinB=QDoubleSpinBox()
                    self.ui.tWTableNotation.setCellWidget(cpt, 2, spinB)
                    cpt += 1
                    # Ci dessous cela permet de "cacher" des info dans la spinbox pour éviter d'aller les chercher dans toutes les cases du tableau
                    spinB.setProperty("nom", nomE)
                    spinB.setProperty("prenom", prenomE)

        self.ui.tWTableNotation.setHorizontalHeaderLabels(['Nom', 'Prénom', 'Note'])

    def ajoutNote(self):
        print("Ajouter Note")
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        dicoEleves= dicoClasse["eleves"]
        print (dicoEleves)
        n = self.ui.tWTableNotation.rowCount()
        for i in range(0, n):
            mat = self.ui.cBMatiereGBNote.currentText()
            eleveTw = self.ui.tWTableNotation.item(i, 0).text()
            spinB = self.ui.tWTableNotation.cellWidget(i, 2)
            note = spinB.value()
            nomDevoir = self.ui.lENomNote.text()
            coeff = self.ui.dSBCoeffNote.value()
            for eleves in dicoEleves:
                if eleves["nom"] == eleveTw:
                    for matiere in eleves["matieres"]:
                        if matiere["nom"] == mat:
                            print(eleves["nom"], matiere["nom"], 'devoir:', nomDevoir, 'coef:', coeff, 'note:', note)
                            ajoutNotes = matiere["notes"]
                            ajoutNotes.append({"nom": nomDevoir, "coef": coeff, "valeur": note})
                            print(ajoutNotes)
        self.sauveJSON(filename)

    def affichNote(self):
        cpt = 0
        self.ui.tWTableNoteModif.clear()
        self.ui.tWTableNoteModif.setColumnCount(3)
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        for eleve in dicoClasse["eleves"]:
            for matiere in eleve["matieres"]:
                mat = self.ui.cBMatiereModifNote.currentText()
                if matiere["nom"] == mat:
                    dicoDevoir = matiere["notes"]
                    for devoir in dicoDevoir:
                        nomDevoir=self.ui.cBListeDevoir.currentText()
                        if devoir["nom"]==nomDevoir :
                            nomE = eleve["nom"]
                            prenomE = eleve["prenom"]
                            valNote=devoir["valeur"]
                            coefNote=devoir["coef"]
                            self.ui.dSBCoeffModifNote.setValue(coefNote)
                            self.ui.tWTableNoteModif.setRowCount(cpt + 1)
                            itemE = QTableWidgetItem(nomE)
                            itemPE = QTableWidgetItem(prenomE)
                            self.ui.tWTableNoteModif.setItem(cpt, 0, itemE)
                            self.ui.tWTableNoteModif.setItem(cpt, 1, itemPE)
                            spinB = QDoubleSpinBox()
                            self.ui.tWTableNoteModif.setCellWidget(cpt, 2, spinB)
                            spinB.setValue(valNote)
                            cpt += 1
        self.ui.tWTableNoteModif.setHorizontalHeaderLabels(['Nom', 'Prénom', 'Note'])

    def modifNote(self):
        print('A faire')
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        n = self.ui.tWTableNoteModif.rowCount()
        for i in range(0, n):
            mat = self.ui.cBMatiereModifNote.currentText()
            eleveTw = self.ui.tWTableNoteModif.item(i, 0).text()
            spinB = self.ui.tWTableNoteModif.cellWidget(i, 2)
            note = spinB.value()
            coeff = self.ui.dSBCoeffNote.value()
            for eleve in dicoClasse["eleves"]:
                if eleve["nom"] == eleveTw:
                    for matiere in eleve["matieres"]:
                        if matiere["nom"] == mat :
                            dicoDevoir = matiere["notes"]
                            for devoir in dicoDevoir:
                                nomDevoir = self.ui.cBListeDevoir.currentText()
                                if devoir["nom"] == nomDevoir:
                                    devoir["valeur"]=note
                                    devoir["coef"]=coeff
            self.sauveJSON(filename)
                            # valDevoir=self.ui.tWTableNoteModif

        # academie = self.ui.cBAcademie.currentIndex()
        # etabliss = self.ui.cBEtablissement.currentIndex()
        # cla = self.ui.cBClasse.currentIndex()
        # dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        # dicoEleves = dicoClasse["eleves"]
        # n = self.ui.tWTableNotation.rowCount()
        # for i in range(0, n):
        #     mat = self.ui.cBMatiereModifNote.currentText()
        #     nomDevoir = self.ui.cBListeDevoir.currentText()
        #     eleveTw = self.ui.tWTableNotation.item(i, 0).text()
        #     spinB = self.ui.tWTableNotation.cellWidget(i, 2)
        #     for eleves in dicoEleves:
        #         if eleves["nom"] == eleveTw:

    def updateEleveBulletin (self):
        self.ui.cBEleveBulletin.clear()
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        for elev in self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"]:
            self.ui.cBEleveBulletin.addItem(elev["nom"])

    def updateApprecia(self):
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        eleveTw = self.ui.cBEleveBulletin.currentIndex()
        dicoMat=dicoClasse["eleves"][eleveTw]["matieres"]
        print(dicoMat)
        n = self.ui.tWBulletin.rowCount()
        for i in range(0, n):
            matTw=self.ui.tWBulletin.item(i, 0).text()
            labelApp=self.ui.tWBulletin.cellWidget(i, 3)
            appreciation=labelApp.text()
            print(matTw)
            for matiere in dicoMat:
                if matiere["nom"] == matTw:
                    matiere["appreciation"]=appreciation
                    self.sauveJSON(filename)

    def calculMoyEleve(self):
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        eleve = self.ui.cBEleveBulletin.currentIndex()
        matEleve = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][eleve]["matieres"]
        dfra = {'Nom': ['Eleve', 'Classe']}
        for m in matEleve:
            notes = m["notes"]
            nomMat = m["nom"]
            sumCoef = 0
            sumNotes = 0
            for n in notes:
                coefNote = n["coef"]
                valeurNote = n["valeur"]
                sumNotes = sumNotes + (coefNote * valeurNote)
                sumCoef = sumCoef + coefNote
                moyEleMat = sumNotes / sumCoef
            dfra.update({nomMat: [moyEleMat]})
        return (dfra)


    def calculMoyClasse(self):
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        eleve = self.ui.cBEleveBulletin.currentIndex()
        matEleve = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][eleve]["matieres"]
        dfrab = {'Nom': ['Eleve', 'Classe']}
        for m in matEleve:
            nomMat = m["nom"]
            dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
            listeNotesCla = []
            nbElevMat = 0
            for eleve in dicoClasse["eleves"]:
                for matiere in eleve["matieres"]:
                    if matiere["nom"] == nomMat:
                        nbElevMat += 1
                        notes = matiere["notes"]
                        nomMat = matiere["nom"]
                        sumCoef = 0
                        sumNotes = 0
                        for n in notes:
                            coefNote = n["coef"]
                            valeurNote = n["valeur"]
                            sumNotes = sumNotes + (coefNote * valeurNote)
                            sumCoef = sumCoef + coefNote
                            moyenneMat = sumNotes / sumCoef
                        listeNotesCla.append(moyenneMat)
                moyClassMat = (sum(listeNotesCla)) / nbElevMat
            dfrab.update({nomMat: [moyClassMat]})
        return (dfrab)


    def affichageMoyEleCla (self):
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        eleve = self.ui.cBEleveBulletin.currentIndex()
        matEleve = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][eleve]["matieres"]
        dfra = {'Nom': ['Eleve', 'Classe']}
        dicoNoteEleve = self.calculMoyEleve()
        dicoNoteClasse = self.calculMoyClasse()
        print(dicoNoteClasse)
        print(dicoNoteEleve)
        for matiere in matEleve:
            nomMatiere = matiere["nom"]
            noteE = dicoNoteEleve[nomMatiere]
            noteC = dicoNoteClasse[nomMatiere]
            print(noteE, noteC)
            dfra.update({nomMatiere: [dicoNoteEleve[nomMatiere][0], dicoNoteClasse[nomMatiere][0]]})
        cpt = 0
        self.ui.tWBulletin.clear()
        self.ui.tWBulletin.setColumnCount(4)
        self.ui.tWBulletin.setHorizontalHeaderLabels(['Matière', 'Moy Elève', 'Moy Classe', 'Appréciation'])
        elev = self.ui.cBEleveBulletin.currentIndex()
        dicoElev = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][elev]
        for matiere in dicoElev["matieres"]:
            nomMatiere = matiere["nom"]
            moyElev = str(round(dfra[nomMatiere][0], 2))
            moyClass = str(round(dfra[nomMatiere][1], 2))
            self.ui.tWBulletin.setRowCount(cpt + 1)
            itemM = QTableWidgetItem(nomMatiere)
            itemMoyE = QTableWidgetItem(moyElev)
            itemMoyC = QTableWidgetItem(moyClass)
            if matiere["appreciation"] != '':
                print(matiere["appreciation"])
                appr = matiere["appreciation"]
                apprec = QLineEdit(appr)
            else:
                apprec = QLineEdit()
            self.ui.tWBulletin.setItem(cpt, 0, itemM)
            self.ui.tWBulletin.setItem(cpt, 1, itemMoyE)
            self.ui.tWBulletin.setItem(cpt, 2, itemMoyC)
            self.ui.tWBulletin.setCellWidget(cpt, 3, apprec)
            cpt += 1
        self.affichageRadar(dfra)


    def affichageRadar(self, moyennes):
        df = pd.DataFrame(moyennes)
        # ------- PART 1: Create background

        # number of variable
        categories = list(df)[1:]
        N = len(categories)

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)

        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([5, 10, 15, 20], ["5", "10", "15", "20"], color="black", size=7)
        plt.ylim(0, 20)

        # ------- PART 2: Add plots
        # Eleve
        values = df.loc[0].drop('Nom').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=1, linestyle='solid', color='green', label="Elève")
        ax.fill(angles, values, 'g', alpha=0.1)

        # Classe
        values = df.loc[1].drop('Nom').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', color='red', label="Classe")
        ax.fill(angles, values, 'r', alpha=0.1)

        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

        # plt.show()
        # plt.tight_layout()
        plt.plot()
        plt.savefig("RadarNotes.png", format='png')

        self.ui.labGraphRadar.setPixmap(QPixmap("RadarNotes.png").scaled(self.ui.labGraphRadar.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        # self.ui.labGraphRadar.setScaledContents(True)

        # self.ui.labGraphRadar.resize(pixmap.width(), pixmap.height())

        plt.clf()

    # Fonction "complete" (calcul moy Eleve, classe, affichage des bulletins et du radar)
    def calculMoyenne (self):
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        eleve=self.ui.cBEleveBulletin.currentIndex()
        matEleve = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][eleve]["matieres"]
        # listeMatEl = []
        # listeNotesEl = []
        dfra = {'Nom': ['Eleve', 'Classe']}
        for m in matEleve:
            notes = m["notes"]
            nomMat = m["nom"]
            sumCoef = 0
            sumNotes = 0
            for n in notes:
                coefNote = n["coef"]
                valeurNote = n["valeur"]
                sumNotes = sumNotes + (coefNote * valeurNote)
                sumCoef = sumCoef + coefNote
                moyEleMat = sumNotes / sumCoef
            # listeNotesEl.append(moyEleMat)
            # listeMatEl.append(nomMat)
            print(m["nom"], moyEleMat)
            dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
            listeMatCla = []
            listeNotesCla = []
            listMatUniqCla = []
            nbElevMat = 0
            for eleve in dicoClasse["eleves"]:
                for matiere in eleve["matieres"]:
                    if matiere["nom"] == nomMat:
                        nbElevMat += 1
                        notes = matiere["notes"]
                        sumCoef = 0
                        sumNotes = 0
                        for n in notes:
                            coefNote = n["coef"]
                            valeurNote = n["valeur"]
                            sumNotes = sumNotes + (coefNote * valeurNote)
                            sumCoef = sumCoef + coefNote
                            moyenneMat = sumNotes / sumCoef
                        listeNotesCla.append(moyenneMat)
                        listeMatCla.append(nomMat)
                        listUniMat = np.unique(listeMatCla)
                        listMatUniqCla.append(listUniMat)
                moyClassMat = (sum(listeNotesCla)) / nbElevMat
            dfra.update({nomMat: [moyEleMat, moyClassMat]})
        print(dfra)
        # def updateBulletin(self):
        cpt = 0
        self.ui.tWBulletin.clear()
        self.ui.tWBulletin.setColumnCount(4)
        self.ui.tWBulletin.setHorizontalHeaderLabels(['Matière', 'Moy Elève', 'Moy Classe', 'Appréciation'])
        elev = self.ui.cBEleveBulletin.currentIndex()
        dicoElev = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][elev]
        for matiere in dicoElev["matieres"]:
            nomMatiere = matiere["nom"]
            moyElev = str(round(dfra[nomMatiere][0],2))
            moyClass = str(round(dfra[nomMatiere][1],2))
            self.ui.tWBulletin.setRowCount(cpt + 1)
            itemM = QTableWidgetItem(nomMatiere)
            itemMoyE = QTableWidgetItem(moyElev)
            itemMoyC = QTableWidgetItem(moyClass)
            if matiere["appreciation"] != '':
                print (matiere["appreciation"])
                appr = matiere["appreciation"]
                apprec = QLineEdit(appr)
            else :
                apprec = QLineEdit()
            self.ui.tWBulletin.setItem(cpt, 0, itemM)
            self.ui.tWBulletin.setItem(cpt, 1, itemMoyE)
            self.ui.tWBulletin.setItem(cpt, 2, itemMoyC)
            self.ui.tWBulletin.setCellWidget(cpt, 3, apprec)
            cpt += 1


        # Prod graphique mpyennes
        df = pd.DataFrame(dfra)
        # ------- PART 1: Create background

        # number of variable
        categories = list(df)[1:]
        N = len(categories)

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)

        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)

        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([5, 10, 15, 20], ["5", "10", "15", "20"], color="black", size=7)
        plt.ylim(0, 20)

        # ------- PART 2: Add plots
        # Eleve
        values = df.loc[0].drop('Nom').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, 'o-', linewidth=1, linestyle='solid', color='green', label="Elève")
        ax.fill(angles, values, 'g', alpha=0.1)

        # Classe
        values = df.loc[1].drop('Nom').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', color='red', label="Classe")
        ax.fill(angles, values, 'r', alpha=0.1)

        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

        # plt.show()
        # plt.tight_layout()
        plt.plot()
        plt.savefig("RadarNotes.png", format='png')

        self.ui.labGraphRadar.setPixmap(QPixmap("RadarNotes.png").scaled(self.ui.labGraphRadar.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
       # self.ui.labGraphRadar.setScaledContents(True)

        # self.ui.labGraphRadar.resize(pixmap.width(), pixmap.height())

        plt.clf()

    # def modifAcad(self):


    def lireJSON(self, fileName):
        with open(fileName) as json_file:
            dico = json.load(json_file)
            return dico
        return None

    def sauveJSON(self, filename):
        jsonClasse = json.dumps(self.mesDatas, sort_keys=True, indent=2)
        f = open(filename, 'w')
        f.write(jsonClasse)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    patate = MainWindow()
    patate.show()
    patate.resize(800,600)

    sys.exit(app.exec_())