# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 09:55:22 2022

@author: Thomas
"""

#=========== IMPORTATION ===========#

import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton,
                             QApplication, QRadioButton,QTextEdit, QMenuBar, QFormLayout, QAction, QWidget,QLabel)
from PyQt5.QtGui import QIcon
from simplex_BigM import *


#===================================#




#============== VIEW ===============#

class View(QWidget):
    '''
        Paramètres : 
            - QWidget est la classe de base de tous les objets d'interface utilisateur.  
            
        But : Gère l'IHM
    '''    
    
    
    def __init__(self, parent = None):
          
       # Héritage - Appel de la classe mère
       super(View, self).__init__(parent)
       
       # Initialisation variable globale
       global nomFichier      
       
       # Stylesheet
       self.stylesheet = open('style.css').read()
       self.setStyleSheet(self.stylesheet)
       
       # Création layout
       self.layout = QFormLayout()
       
       # Menu bar
       self.menu = QMenuBar()
       self.menu.setStyleSheet(self.stylesheet)
       self.menuFichier = self.menu.addMenu("Fichier") 
       self.layout.addRow(self.menu)

      
       # Action sous menu Quitter
       quitterMenu = QAction(QIcon('Logo\exit.png'),'   Quitter', self)
       quitterMenu.setShortcut('Ctrl+Q')
       quitterMenu.triggered.connect(app.quit)
       quitterMenu.triggered.connect(self.close)
       self.menuFichier.addAction(quitterMenu)
       
       self.question = QLabel('Quelle question ?')
       self.quest1 = QRadioButton('Question n°1')
       self.quest2 = QRadioButton('Question n°2')
       self.quest3 = QRadioButton('Question n°3')
       self.layout.addRow(self.question)
       self.layout.addRow(self.quest1)
       self.layout.addRow(self.quest2)
       self.layout.addRow(self.quest3)
       
 
       
       self.equation = QTextEdit(self)
       self.layout.addRow(self.equation)

    
       # Texte liste routeur
       self.textList = QLabel("\n Veuillez saisir les données suivantes :\n")
       self.layout.addRow(self.textList)
       
       self.maxMin = QLabel(self)
       self.maxMin.setText("S'agit-il d'une maximisation ou minimisation (Schéma : max ou min) :")
       self.lineMaxMin = QLineEdit(self)
       self.layout.addRow(self.maxMin)
       self.layout.addRow(self.lineMaxMin)       
       
       self.coeffMulti = QLabel(self)
       self.coeffMulti.setText('Coefficients multiplicateurs de la fonction (Schéma : coeff1,coeff2,coeff3 ...) :')
       self.lineCoeffMulti = QLineEdit(self)
       self.layout.addRow(self.coeffMulti)
       self.layout.addRow(self.lineCoeffMulti)
       
       self.coeffMultiContrainte = QLabel(self)
       self.coeffMultiContrainte.setText('Coefficients multiplicateurs des contraintes (Schéma : coeff1Contrainte1,coeff2Contrainte1,... coeff1Contrainte2,coeff2Contrainte2,...  ) :')
       self.lineCoeffMultiContrainte = QLineEdit(self)
       self.layout.addRow(self.coeffMultiContrainte)
       self.layout.addRow(self.lineCoeffMultiContrainte)
       
       self.resultatContrainte = QLabel(self)
       self.resultatContrainte.setText('Les résultats des contraintes (Schéma : res1,res2,res3 ...) :')
       self.lineResultatContrainte = QLineEdit(self)
       self.layout.addRow(self.resultatContrainte)
       self.layout.addRow(self.lineResultatContrainte)
       
       self.signeContrainte = QLabel(self)
       self.signeContrainte.setText("Inégalité ou égalité ? (Règle : -1:'<=', 1:'>=', 0:'='   Schéma : chiffre1,chiffre2, ... :")
       self.lineSigneContrainte = QLineEdit(self)
       self.layout.addRow(self.signeContrainte)
       self.layout.addRow(self.lineSigneContrainte)
          
       # Création des boutons        
       self.buttonLaunch = QPushButton("Calculer")
       self.buttonLaunch.setStyleSheet(self.stylesheet)
       
       self.layout.addRow(self.buttonLaunch)
       self.setLayout(self.layout)
       

       # Gestion des events
       self.buttonLaunch.clicked.connect(lambda: self.btn_clickLaunch())
       
       self.quest1.toggled.connect(lambda: self.btn_clickQuest(1))
       self.quest1.setChecked(True)
       self.quest2.toggled.connect(lambda: self.btn_clickQuest(2))
       self.quest3.toggled.connect(lambda: self.btn_clickQuest(3))
       
       
       self.setWindowTitle("Accueil")
       self.show()
       self.setGeometry(500, 200, 500, 550)
       
       

    def btn_clickLaunch(self):
        '''
            But : Gère la récupération des champs et appelle la fonction de Simplex
        '''    
        champ1 = self.lineCoeffMulti.text()
        champ1 = champ1.split(',')
        champ1 = [int(i) for i in champ1]
        print(champ1)
        
        champ2 = self.lineCoeffMultiContrainte.text()
        champ2 = champ2.split(' ')
        champ2 = [i.split(',') for i in champ2]
        
        for i in range(len(champ2)):
            for k in range(len(champ2[i])):
                champ2[i][k] = float(champ2[i][k])
        print(champ2)

        
        champ3 = self.lineResultatContrainte.text()
        champ3 = champ3.split(',')
        champ3 = [int(i) for i in champ3]
        print(champ3)
        
        champ4 = self.lineSigneContrainte.text()
        champ4 = champ4.split(',')
        champ4 = [int(i) for i in champ4]
        print(champ4)
        
        champ5 = self.lineMaxMin.text()

        affichage = 1
        simplex_BigM(champ2,champ3,champ1,champ4,champ5,affichage)


    def btn_clickQuest(self,choix):
        '''
            But : Gère le switch des questions via les boutons radios, complète les champs nécessaires
        '''    
        texte = ""
        if(choix == 1):
            texte = "Énoncé : \nMAX Z = 11x1 + 16x2 + 15x3 avec contrainte n°1 : x1 + 2x2  + 3/2x3 <= 12000, contrainte n°2 : 2/3x1 + 2/3x2 + x3 <= 4600 et contrainte n°3 : 1/2x1 +1/3x2 +1/2x3 <= 2400 "
            champ1 = "11,16,15"
            champ2 = "1,2,1.5 0.6666666666,0.666666666666,1 0.5,0.3333333333333,0.5"
            champ3 = "12000,4600,2400"
            champ4 = "-1,-1,-1"
            champ5 = "max"
        
        elif(choix == 2):
            texte = "Énoncé : \nMAX Z = -20000x1 -25000x2 avec contrainte n°1 : 400x1 + 300x2 >= 25000, contrainte n°2 : 300x1 + 400x2 >= 27000 et contrainte n°3 : 200x1 + 500x2 >= 30000 "
            champ1 = "-20000,-25000"
            champ2 = "400,300 300,400 200,500"
            champ3 = "25000,27000,30000"
            champ4 = "1,1,1"
            champ5 = "max"
        
        elif(choix == 3):
            texte = "Énoncé : \nMIN Z = 30x1 + 36x2 + 25x3 + 30x4 avec contrainte n°1 : x1 + x2 = 200, contrainte n°2 : x3 + x4 = 300, contrainte n°3 : x1 + x3 <= 400 et contrainte n°4 : x2 + x4 <= 300 "
            champ1 = "30,36,25,30"
            champ2 = "1,1,0,0 0,0,1,1 1,0,1,0 0,1,0,1"
            champ3 = "200,300,400,300"
            champ4 = "0,0,-1,-1"
            champ5 = "min"
        
        self.lineMaxMin.setText(champ5)
        self.lineCoeffMulti.setText(champ1)
        self.lineCoeffMultiContrainte.setText(champ2)
        self.lineResultatContrainte.setText(champ3)
        self.lineSigneContrainte.setText(champ4)
        self.equation.setText(texte)


        
if __name__ == '__main__':
   app = QApplication(sys.argv)
   view = View()
   sys.exit(app.exec_())