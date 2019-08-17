import sys, json
from PySide2.QtWidgets import (QLabel, QApplication, QDoubleSpinBox, QTableWidgetItem, QLineEdit, QInputDialog, QGroupBox, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy,QMainWindow)
# from PySide2.QtGui import QPixmap
import numpy as np
import pandas as pd
import numpy as np
from math import pi
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
        self.ui.pBValAppr.clicked.connect(self.updateApprecia)
        self.ui.pBValCalculMoy.clicked.connect(self.calculMoyenne)

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
        # self.ui.cBMatiereBulletin.addItems(listeMatieresUniques)

    def ajoutAcademie (self):
        print("Ajout Académie")
        fiche = {}
        fiche["nom"]= self.ui.lENomAcad.text()
        fiche["etablissements"]=[]
        # [{"nom":str(), "adresse":str(),"classes":[{"nom":str(), "anneeSco":str(), "PP":str(), "eleves":[{"nom":str(), "prenom":str(), "adresse":str(), "appreciationPP":str(), "matieres":[{"nom":str(), "coef" : float(), "appreciation":str(), "notes": []}]}]}]}]
        # {"nom": str(), "anneeSco": str(), "PP": str(), "eleves": [{"nom": str(), "prenom": str(), "adresse": str(),"appreciationPP": str(), "matieres": [{"nom": str(), "coef": float(), "appreciation": str(), "notes": []}]}]}
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
        ficheE["adresse"]=self.ui.lEEtabAdress.text()
        ficheE["classes"]=[]
        # [{"nom":str(), "anneeSco":str(), "PP":str(), "eleves":[{"nom":str(), "prenom":str(), "adresse":str(), "appreciationPP":str(), "matieres":[]}]}]
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
        # [{"nom":str(), "prenom":str(), "adresse":str(), "appreciationPP":str(), "matieres":[{"nom":str(), "coef" : float(), "appreciation":str(), "notes": []}]}]
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

    def updateApprecia(self):
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        dicoEleves = dicoClasse["eleves"]
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
                    print('ok')
                    self.sauveJSON(filename)



    def calculMoyenne (self):
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasse.currentIndex()
        eleve=self.ui.cBEleveBulletin.currentIndex()
        matEleve = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][eleve]["matieres"]
        listeMatEl = []
        listeNotesEl = []
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
            listeNotesEl.append(moyEleMat)
            listeMatEl.append(nomMat)
            # listeMatNotEle = {"nom":}
            print(m["nom"], moyEleMat)
            dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
            listeMatCla = []
            listeNotesCla = []
            listMatUniqCla = []
            nbElevMat = 0
            for eleve in dicoClasse["eleves"]:
                # print(eleve["nom"])
                for matiere in eleve["matieres"]:
                    mat = nomMat
                    # print(matiere["nom"])
                    if matiere["nom"] == mat:
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
                        # print(nomMat, moyenneMat)
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
        # academie = self.ui.cBAcademie.currentIndex()
        # etabliss = self.ui.cBEtablissement.currentIndex()
        # cla = self.ui.cBClasse.currentIndex()
        elev = self.ui.cBEleveBulletin.currentIndex()
        dicoElev = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][elev]
        for matiere in dicoElev["matieres"]:
            nomMatiere = matiere["nom"]
            moyElev = str(dfra[nomMatiere][0])
            moyClass = str(dfra[nomMatiere][1])
            self.ui.tWBulletin.setRowCount(cpt + 1)
            itemM = QTableWidgetItem(nomMatiere)
            itemMoyE = QTableWidgetItem(moyElev)
            itemMoyC = QTableWidgetItem(moyClass)
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
        plt.yticks([5, 10, 15, 20], ["5", "10", "15", "20"], color="#8A2BE2", size=7)
        plt.ylim(0, 20)

        # ------- PART 2: Add plots
        # Eleve
        values = df.loc[0].drop('Nom').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', color='blue', label="Elève")
        ax.fill(angles, values, 'b', alpha=0.1)

        # Classe
        values = df.loc[1].drop('Nom').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', color='red', label="Classe")
        ax.fill(angles, values, 'r', alpha=0.1)

        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

        plt.show()

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