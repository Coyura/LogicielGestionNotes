import sys, json
from PySide2.QtWidgets import (QLabel, QApplication, QDoubleSpinBox, QTableWidgetItem, QInputDialog, QGroupBox, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy,QMainWindow)
# from PySide2.QtGui import QPixmap
import numpy as np
# import matplotlib.pyplot as plt
# from io import BytesIO
# import base64
from ui_designLogicielFinal import Ui_MainWindow

filename = "dataNotes.json"

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        global filename
        self.mesDatas = {}

        self.mesDatas = self.lireJSON(filename)

        #Il faut maintenant charger les établissements de l'académie choisie :
        self.ui.cBAcademie.currentIndexChanged.connect(self.updateEtablissement)

        #Il faut maintenant charger les classes de l'établissement choisie :
        self.ui.cBEtablissement.currentIndexChanged.connect(self.updateClasse)

        self.ui.cBClasse.currentIndexChanged.connect(self.updateMatiere)
        self.ui.cBClasseGPNote.currentIndexChanged.connect(self.updateMatiere)
        self.ui.cBMatiereGBNote.currentIndexChanged.connect(self.updateSaisieEleve)

        self.ui.pBValiderNotation.clicked.connect(self.ajoutNote)

        self.ui.pBNoterNote.clicked.connect(self.ajoutAcademie)
        self.ui.pBModifierNote.clicked.connect(self.ajoutEtablissement)


        # Il faut charger les académies dans la comboBox:
        self.updateAcademie()

    def updateAcademie (self):
        for acad in self.mesDatas["academies"]:
            self.ui.cBAcademie.addItem(acad["nom"])
            print(acad["nom"])

    def ajoutAcademie (self):
        print("Ajout Académie")

        retour = QInputDialog().getText(self, "Ajout Académie", "Nom")
        if retour[0] == "":
            return
        fiche = {}
        fiche["nom"] = retour[0]
        fiche["etablissements"]=""
        self.mesDatas["academies"].append(fiche)
        print(fiche)

        self.ui.cBAcademie.addItem(fiche["nom"])
        self.sauveJSON(filename)

    def ajoutEtablissement(self):
        print("Ajout Etablissement")

    def sauveJSON (self, filename):
        jsonClasse=json.dumps(self.mesDatas, sort_keys=True, indent=2)
        f=open(filename, 'w')
        f.write(jsonClasse)

    def updateEtablissement(self):
        self.ui.cBEtablissement.clear()
        academie = self.ui.cBAcademie.currentIndex()
        for etab in self.mesDatas["academies"][academie]["etablissements"]:
            self.ui.cBEtablissement.addItem(etab["nom"])
            print(etab["nom"])

    def updateClasse(self):
        self.ui.cBClasse.clear()
        self.ui.cBClasseGPNote.clear()
        self.ui.cBClasseGPNote.clear()
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        for cla in self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"]:
            self.ui.cBClasse.addItem(cla["nom"])
            self.ui.cBClasseGPNote.addItem(cla["nom"])

    def updateMatiere (self) :
        self.ui.cBMatiereGBNote.clear()
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasseGPNote.currentIndex()
        listeMatieres = []
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        for eleve in dicoClasse["eleves"]:
            for matiere in eleve["matieres"]:
                listeMatieres.append(matiere["nom"])
        listeMatieresUniques = np.unique(listeMatieres)
        self.ui.cBMatiereGBNote.addItems(listeMatieresUniques)

    def ajoutNote(self):
        print("Ajouter Note")
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasseGPNote.currentIndex()
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
                            ajoutNotes.append({"nom": nomDevoir, "coefficient": coeff, "valeur": note})
                            print(ajoutNotes)
                            self.sauveJSON(filename)
                            
        # for eleve in dicoClasse["eleves"]:
        #     for matiere in eleve["matieres"]:
        #         mat = self.ui.cBMatiereGBNote.currentText()
        #         if matiere["nom"] == mat:
        #             nomE = eleve["nom"]
        #             print(nomE)
        #             dicoM = matiere["nom"]
        #             print(dicoM)
        #             dicoDevoir=matiere["notes"]
        #             print (dicoDevoir)
        #             newDevoir={}
        #             newDevoir["nom"]=self.ui.lENomNote.text()
        #             newDevoir["coef"]=float(self.ui.lECoeffNote.text())
        #             newDevoir["valeur"]=15.0
        #             print(newDevoir)
        #             self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]["eleves"][nomE]["matieres"][mat]["notes"].append(newDevoir)


    def updateSaisieEleve(self):
        cpt=0
        self.ui.tWTableNotation.clear()
        # self.ui.tWTableNotation.setColumnCount(2)
        # ça permettait de définir le nombre de colonne de la tableWidget si non défini dans le QtDesigner
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        cla = self.ui.cBClasseGPNote.currentIndex()
        dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        for eleve in dicoClasse["eleves"]:
            for matiere in eleve["matieres"]:
                mat=self.ui.cBMatiereGBNote.currentText()
                if matiere["nom"]==mat:
                    nomE = eleve["nom"]
                    self.ui.tWTableNotation.setRowCount(cpt+1)
                    itemE=QTableWidgetItem(nomE)
                    self.ui.tWTableNotation.setItem(cpt,0,itemE)
                    # utiliser le QDoubleSpin permet de rentrer une note en transformant direct en float
                    spinB=QDoubleSpinBox()
                    spinB.setProperty("nom", nomE)
                    self.ui.tWTableNotation.setCellWidget(cpt,1, spinB)
                    cpt += 1

        self.ui.tWTableNotation.setHorizontalHeaderLabels(['Nom', 'Note'])


    def lireJSON(self, fileName):
        with open(fileName) as json_file:
            dico = json.load(json_file)
            return dico
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)

    patate = MainWindow()
    patate.show()

    sys.exit(app.exec_())


# if __name__ == '__main__':
#     # Create the Qt Application
#     app = QApplication(sys.argv)
#     # Create and show the form
#     voy = Voyage()
#     voy.show()
#     # Run the main Qt loop
#     sys.exit(app.exec_())