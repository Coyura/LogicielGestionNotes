import sys, json
from PySide2.QtWidgets import (QLabel, QApplication, QDoubleSpinBox, QTableWidgetItem, QGroupBox, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy,QMainWindow)
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

        self.ui.pBNoterNote.clicked.connect(self.ajoutNoteDevoir)

        # Il faut charger les académies dans la comboBox:
        self.updateAcademie()

    def updateAcademie (self):
        for acad in self.mesDatas["academies"]:
            self.ui.cBAcademie.addItem(acad["nom"])

    def updateEtablissement(self):
        self.ui.cBEtablissement.clear()
        academie = self.ui.cBAcademie.currentIndex()
        for etab in self.mesDatas["academies"][academie]["etablissements"]:
            self.ui.cBEtablissement.addItem(etab["nom"])

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

    def ajoutNoteDevoir(self):
        print("Ajouter devoir")
        # academie = self.ui.cBAcademie.currentIndex()
        # etabliss = self.ui.cBEtablissement.currentIndex()
        # cla = self.ui.cBClasseGPNote.currentIndex()
        # dicoClasse = self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"][cla]
        # for eleve in dicoClasse["eleves"]:
        #     for matiere in eleve["matieres"]:
        #         mat = self.ui.cBMatiereGBNote.currentText()
        #         if matiere["nom"] == mat:
        #             nomE = eleve["nom"]


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