# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designLogicielFinal.ui',
# licensing of 'designLogicielFinal.ui' applies.
#
# Created: Fri Jul 26 09:37:46 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1665, 875)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.verticalLayout_12.addLayout(self.verticalLayout_10)
        self.cBAcademie = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBAcademie.sizePolicy().hasHeightForWidth())
        self.cBAcademie.setSizePolicy(sizePolicy)
        self.cBAcademie.setMaximumSize(QtCore.QSize(300, 16777215))
        self.cBAcademie.setObjectName("cBAcademie")
        self.verticalLayout_12.addWidget(self.cBAcademie)
        self.cBEtablissement = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBEtablissement.sizePolicy().hasHeightForWidth())
        self.cBEtablissement.setSizePolicy(sizePolicy)
        self.cBEtablissement.setMinimumSize(QtCore.QSize(300, 0))
        self.cBEtablissement.setObjectName("cBEtablissement")
        self.verticalLayout_12.addWidget(self.cBEtablissement)
        self.cBClasse = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cBClasse.sizePolicy().hasHeightForWidth())
        self.cBClasse.setSizePolicy(sizePolicy)
        self.cBClasse.setMaximumSize(QtCore.QSize(300, 300))
        self.cBClasse.setObjectName("cBClasse")
        self.verticalLayout_12.addWidget(self.cBClasse)
        self.pBGestNote = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBGestNote.sizePolicy().hasHeightForWidth())
        self.pBGestNote.setSizePolicy(sizePolicy)
        self.pBGestNote.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pBGestNote.setObjectName("pBGestNote")
        self.verticalLayout_12.addWidget(self.pBGestNote)
        self.pBMoyenne = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBMoyenne.sizePolicy().hasHeightForWidth())
        self.pBMoyenne.setSizePolicy(sizePolicy)
        self.pBMoyenne.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pBMoyenne.setObjectName("pBMoyenne")
        self.verticalLayout_12.addWidget(self.pBMoyenne)
        self.pBBulletin = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pBBulletin.sizePolicy().hasHeightForWidth())
        self.pBBulletin.setSizePolicy(sizePolicy)
        self.pBBulletin.setMaximumSize(QtCore.QSize(300, 300))
        self.pBBulletin.setObjectName("pBBulletin")
        self.verticalLayout_12.addWidget(self.pBBulletin)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem)
        self.horizontalLayout_9.addLayout(self.verticalLayout_12)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 20, 501, 621))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.cBClasseGPNote = QtWidgets.QComboBox(self.verticalLayoutWidget_9)
        self.cBClasseGPNote.setObjectName("cBClasseGPNote")
        self.verticalLayout.addWidget(self.cBClasseGPNote)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.cBMatiereGBNote = QtWidgets.QComboBox(self.verticalLayoutWidget_9)
        self.cBMatiereGBNote.setObjectName("cBMatiereGBNote")
        self.verticalLayout_5.addWidget(self.cBMatiereGBNote)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.lENomNote = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.lENomNote.setObjectName("lENomNote")
        self.verticalLayout_2.addWidget(self.lENomNote)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.lECoeffNote = QtWidgets.QLineEdit(self.verticalLayoutWidget_9)
        self.lECoeffNote.setObjectName("lECoeffNote")
        self.verticalLayout_3.addWidget(self.lECoeffNote)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_15.addItem(spacerItem2)
        self.pBNoterNote = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.pBNoterNote.setObjectName("pBNoterNote")
        self.verticalLayout_15.addWidget(self.pBNoterNote)
        self.horizontalLayout_2.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_16.addItem(spacerItem3)
        self.pBModifierNote = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.pBModifierNote.setObjectName("pBModifierNote")
        self.verticalLayout_16.addWidget(self.pBModifierNote)
        self.horizontalLayout_2.addLayout(self.verticalLayout_16)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.tWTableNotation = QtWidgets.QTableWidget(self.verticalLayoutWidget_9)
        self.tWTableNotation.setObjectName("tWTableNotation")
        self.tWTableNotation.setColumnCount(2)
        self.tWTableNotation.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tWTableNotation.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tWTableNotation.setHorizontalHeaderItem(1, item)
        self.verticalLayout_9.addWidget(self.tWTableNotation)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pBValiderNotation = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.pBValiderNotation.setObjectName("pBValiderNotation")
        self.horizontalLayout_3.addWidget(self.pBValiderNotation)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(10, 20, 531, 621))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.cBMatiereBulletin = QtWidgets.QComboBox(self.verticalLayoutWidget_11)
        self.cBMatiereBulletin.setObjectName("cBMatiereBulletin")
        self.verticalLayout_7.addWidget(self.cBMatiereBulletin)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_8.addWidget(self.label_14)
        self.cBEleveBulletin = QtWidgets.QComboBox(self.verticalLayoutWidget_11)
        self.cBEleveBulletin.setObjectName("cBEleveBulletin")
        self.verticalLayout_8.addWidget(self.cBEleveBulletin)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.tWBulletin = QtWidgets.QTableWidget(self.verticalLayoutWidget_11)
        self.tWBulletin.setObjectName("tWBulletin")
        self.tWBulletin.setColumnCount(4)
        self.tWBulletin.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tWBulletin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tWBulletin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tWBulletin.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tWBulletin.setHorizontalHeaderItem(5, item)
        self.verticalLayout_11.addWidget(self.tWBulletin)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(100, 0))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.labGraphRadar = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labGraphRadar.sizePolicy().hasHeightForWidth())
        self.labGraphRadar.setSizePolicy(sizePolicy)
        self.labGraphRadar.setMinimumSize(QtCore.QSize(400, 0))
        self.labGraphRadar.setObjectName("labGraphRadar")
        self.verticalLayout_11.addWidget(self.labGraphRadar)
        self.horizontalLayout_9.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1665, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "LogiNotes", None, -1))
        self.pBGestNote.setText(QtWidgets.QApplication.translate("MainWindow", "Gestion des notes", None, -1))
        self.pBMoyenne.setText(QtWidgets.QApplication.translate("MainWindow", "Moyennes", None, -1))
        self.pBBulletin.setText(QtWidgets.QApplication.translate("MainWindow", "Bulletins", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Gestion des Notes", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Gestion des notes", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Classe :", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Noter Devoir", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("MainWindow", "Matière :", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Nom Devoir :", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Coefficient :", None, -1))
        self.pBNoterNote.setText(QtWidgets.QApplication.translate("MainWindow", "Noter", None, -1))
        self.pBModifierNote.setText(QtWidgets.QApplication.translate("MainWindow", "Modifier", None, -1))
        self.tWTableNotation.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Elève :", None, -1))
        self.tWTableNotation.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Note :", None, -1))
        self.pBValiderNotation.setText(QtWidgets.QApplication.translate("MainWindow", "Valider", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Moyennes - Bulletin", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate("MainWindow", "Moyennes Globales", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("MainWindow", "Matère :", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate("MainWindow", "Elève :", None, -1))
        self.tWBulletin.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Matière", None, -1))
        self.tWBulletin.horizontalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "Nom - Prénom ", None, -1))
#        self.tWBulletin.horizontalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "Moy Elève", None, -1))
#        self.tWBulletin.horizontalHeaderItem(5).setText(QtWidgets.QApplication.translate("MainWindow", "Appréciation", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "Moyennes", None, -1))
        self.labGraphRadar.setText(QtWidgets.QApplication.translate("MainWindow", "Graphique", None, -1))
