import sys, json
from PySide2.QtWidgets import (QLabel, QApplication, QDoubleSpinBox, QTableWidgetItem, QInputDialog, QGroupBox, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy,QMainWindow)
# from PySide2.QtGui import QPixmap
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
# import matplotlib.pyplot as plt
# from io import BytesIO
# import base64
from ui_designLogicielFinalV2 import Ui_MainWindow

filename = "dataNotesV2.json"

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global filename
        self.mesDatas = {}

        self.mesDatas = self.lireJSON(filename)

        # Il faut maintenant charger les établissements de l'académie choisie :
        self.ui.cBAcademie.currentIndexChanged.connect(self.updateEtablissement)

        # Il faut maintenant charger les classes de l'établissement choisie :
        self.ui.cBEtablissement.currentIndexChanged.connect(self.updateClasse)

        self.ui.cBClasse.currentIndexChanged.connect(self.updateMatiere)
        ## self.ui.cBClasseGPNote.currentIndexChanged.connect(self.updateMatiere)
        self.ui.cBMatiereGBNote.currentIndexChanged.connect(self.updateSaisieEleve)

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

        # Calcul Moyennes Eleve
        self.ui.cBEleveBulletin.currentIndexChanged.connect(self.calculMoyenne)

        # Il faut charger les académies dans la comboBox:
        self.updateAcademie()

        # Chargement de la liste des élèves d'une matière pour bulletin
        self.ui.cBClasse.currentIndexChanged.connect(self.updateEleveBulletin)

    def updateAcademie (self):
        for acad in self.mesDatas["academies"]:
            self.ui.cBAcademie.addItem(acad["nom"])
            self.ui.cBListAcad.addItem(acad["nom"])
            self.ui.cBListAcadClass.addItem(acad["nom"])
            self.ui.cBListAcadEleve.addItem(acad["nom"])
            print(acad["nom"])

    def updateEtablissement(self):
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
        self.ui.cBMatiereBulletin.clear()
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
        self.ui.cBMatiereBulletin.addItems(listeMatieresUniques)

    def ajoutAcademie (self):
        print("Ajout Académie")

        # retour = QInputDialog().getText(self, "Ajout Académie", "Nom")
        # if retour[0] == "":
        #     return
        fiche = {}
        # fiche["nom"] = retour[0]
        # fiche["etablissements"]=""
        fiche["nom"]= self.ui.lENomAcad.text()
        self.mesDatas["academies"].append(fiche)
        self.sauveJSON(filename)
        print(fiche)

        self.ui.cBAcademie.addItem(fiche["nom"])
        self.ui.cBListAcad.addItem(fiche["nom"])
        self.ui.cBListAcadClass.addItem(fiche["nom"])
        self.ui.cBListAcadEleve.addItem(fiche["nom"])

    def ajoutEtablissement(self):
        print("Ajout Etablissement")
        ficheE = {}
        academie = self.ui.cBListAcad.currentIndex()
        dicoEtab=self.mesDatas["academies"][academie]["etablissements"]
        ficheE["nom"]=self.ui.lENomEtab.text()
        dicoEtab.append(ficheE)
        self.sauveJSON(filename)
        print(ficheE)

        self.ui.cBEtablissement.addItem(ficheE["nom"])
        # self.ui.cBListEtabClass.addItem(ficheE["nom"])
        # self.ui.cBListEtabEleve.addItem(ficheE["nom"])

    def ajoutClasse(self):
        print("Ajout Classe")
        ficheC = {}
        academie = self.ui.cBListAcadClass.currentIndex()
        etab = self.ui.cBListEtabClass.currentIndex()
        dicoClasse=self.mesDatas["academies"][academie]["etablissements"][etab]["classes"]
        ficheC["nom"]=self.ui.lENomClasse.text()
        dicoClasse.append(ficheC)
        self.sauveJSON(filename)
        print(ficheE)

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
        # ficheE["prenom"]=self.ui.lEPrenomEleve.text()
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

    def updateSaisieEleve(self):
        print ("prout")
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
                    spinB.setProperty("nom", nomE)
                    spinB.setProperty("prenom", prenomE)
                    self.ui.tWTableNotation.setCellWidget(cpt,2, spinB)
                    cpt += 1
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
            spinB = self.ui.tWTableNotation.cellWidget(i, 1)
            note = spinB.value()
            nomDevoir = self.ui.lENomNote.text()
            coeff =  float(self.ui.lECoeffNote.text())
            for eleves in dicoEleves:
                if eleves["nom"] == eleveTw:
                    for matiere in eleves["matieres"]:
                        if matiere["nom"] == mat:
                            print(eleves["nom"], matiere["nom"], 'devoir:', nomDevoir, 'coeff:', coeff, 'note:', note)
                            ajoutNotes = matiere["notes"]
                            ajoutNotes.append({"nom": nomDevoir, "coef": coeff, "valeur": note})
                            print(ajoutNotes)
                            self.sauveJSON(filename)

    def updateEleveBulletin (self):
        self.ui.cBEleveBulletin.clear()
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        for elev in self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"]:
            self.ui.cBEleveBulletin.addItem(elev["nom"])

    def calculMoyenne (self):
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        eleve=self.ui.cBEleveBulletin.currentIndex()
        matEleve = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][eleve]["matieres"]
        # noteMatEleve = mesDatas["academies"][0]["etablissements"][0]["classes"][0]["eleves"][0]["matieres"][0]["notes"]
        for m in matEleve:
            notes = m["notes"]
            sumCoef = 0
            sumNotes = 0
            for n in notes:
                coefNote = n["coef"]
                valeurNote = n["valeur"]
                sumNotes = sumNotes + (coefNote * valeurNote)
                sumCoef = sumCoef + coefNote
                moyenneMat = sumNotes / sumCoef
                print(m["nom"], moyenneMat)

        # dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        # for eleve in dicoClasse["eleves"]:
        #     for matiere in eleve["matieres"]:
        #         mat = self.ui.cBMatiereBulletin.currentText()
        #         if matiere["nom"] == mat:
        #             nomE = eleve["nom"]
        #             self.ui.cBEleveBulletin.addItem(nomE)

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

    sys.exit(app.exec_())