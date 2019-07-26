import sys, json
from PySide2.QtWidgets import (QLabel, QApplication, QVBoxLayout, QWidget, QComboBox, QHBoxLayout, QSizePolicy,QMainWindow)
# from PySide2.QtGui import QPixmap
# import numpy as np
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

        #Il faut maintenant charger les établissements de l'académie choisie :
        self.ui.cBEtablissement.currentIndexChanged.connect(self.updateClasse)

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
        academie = self.ui.cBAcademie.currentIndex()
        etabliss = self.ui.cBEtablissement.currentIndex()
        for cla in self.mesDatas["academies"][academie]["etablissements"][etabliss]["classes"]:
            self.ui.cBClasse.addItem(cla["nom"])


    def lireJSON(self, fileName):
        with open(fileName) as json_file:
            dico = json.load(json_file)
            return dico
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


# if __name__ == '__main__':
#     # Create the Qt Application
#     app = QApplication(sys.argv)
#     # Create and show the form
#     voy = Voyage()
#     voy.show()
#     # Run the main Qt loop
#     sys.exit(app.exec_())