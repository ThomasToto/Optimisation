import sys
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
                             qApp , QMainWindow,QApplication, QMainWindow, 
                             QWidget, QRadioButton, QLabel, QGridLayout,
                             QComboBox)

import Question1_PasFixe, Question1_PasAccelere, Question1_Bissectrice, Question2_Newton_Raphson

class Home(QWidget):
    
    def __init__(self):
        super().__init__()
        
        # Stylesheet
        self.stylesheet = open('style.css').read()
        self.setStyleSheet(self.stylesheet)
        
        
        self.setWindowTitle('Accueil')
        self.l1 = QLabel("Quelle question ?")
        self.ch1 = QRadioButton("Question 1")
        self.ch2 = QRadioButton("Question 2")
        self.beg = QPushButton("Suivant")
        self.space = QLabel()
        self.init_ui()
        
        
    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.space)
        v_box.addWidget(self.l1)
        v_box.addWidget(self.ch1)
        v_box.addWidget(self.ch2)
        v_box.addWidget(self.space)
        v_box.addWidget(self.beg)
        
        self.setLayout(v_box)
        self.show()
        
        self.beg.clicked.connect(self.begin)
        
    def begin(self):
        if self.ch1.isChecked():
            self.choice = Q1()
            self.choice.show()
        if self.ch2.isChecked():
            self.choice = Q2()
            self.choice.show()
            
class Q1(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.stylesheet = open('style.css').read()
        self.setStyleSheet(self.stylesheet)
        self.setWindowTitle('Question 1')
        self.l1 = QLabel("Quelle méthode ? ")
        self.ch1 = QRadioButton("Pas fixe")
        self.ch2 = QRadioButton("Pas accéléré")
        self.ch3 = QRadioButton("Méthode de la bissection")
        self.beg = QPushButton("Suivant")
        self.space = QLabel()
        self.init_ui()

    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.space)
        v_box.addWidget(self.l1)
        v_box.addWidget(self.ch1)
        v_box.addWidget(self.ch2)
        v_box.addWidget(self.ch3)
        v_box.addWidget(self.space)
        v_box.addWidget(self.beg)
        
        self.setLayout(v_box)
        self.beg.clicked.connect(self.param)
        self.show()
    
    def param(self):
        if self.ch1.isChecked():
            self.parameters = Parameters('fixe')
        elif self.ch2.isChecked():
            self.parameters = Parameters('accel')
        elif self.ch3.isChecked():
            self.parameters = Parameters('bissec')
        self.parameters.show()
            

class Parameters(QWidget):
    
    def __init__(self,method):
        super().__init__()
        self.stylesheet = open('style.css').read()
        self.setStyleSheet(self.stylesheet)
        self.method = method
        self.setWindowTitle('Paramètres')
        self.l0 = QLabel("Vous cherchez des extremums de la fonction : ")
        self.l1 = QLabel("x^5 -5x^3 -20x +5")
        self.space = QLabel()
        self.extrem = QLabel("Quel extremum ?")
        self.min = QRadioButton('Minimum')
        self.min.setChecked(True)
        self.max = QRadioButton('Maximum')
        self.dep = QLabel('Point de départ :')
        self.depart = QLineEdit('0')
        self.pa = QLabel('Pas de départ : ')
        self.pas = QLineEdit('0.05')
        self.prec = QLabel('Précision (entre 0 et 1) :')
        self.preci = QLineEdit('0.1')
        self.inter = QLabel('Intervalle de départ (liste) : ')
        self.interval1 = QLineEdit('0')
        self.interval2 = QLineEdit('5')
        self.calcul = QPushButton('Calculer')
        self.init_ui()
    
    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.l0)
        v_box.addWidget(self.l1)
        v_box.addWidget(self.space)
        v_box.addWidget(self.extrem)
        v_box.addWidget(self.min)
        v_box.addWidget(self.max)
        v_box.addWidget(self.space)
        
        h_dep = QHBoxLayout()
        h_dep.addWidget(self.dep)
        h_dep.addWidget(self.depart)
        
        h_pa = QHBoxLayout()
        h_pa.addWidget(self.pa)
        h_pa.addWidget(self.pas)
        
        h_prec = QHBoxLayout()
        h_prec.addWidget(self.prec)
        h_prec.addWidget(self.preci)
        
        h_inter = QHBoxLayout()
        h_inter.addWidget(self.inter)
        h_inter.addWidget(self.interval1)
        h_inter.addWidget(self.interval2)
        
        
        if self.method == 'bissec':
            v_box.addLayout(h_inter)
            v_box.addLayout(h_prec)
        else:
            v_box.addLayout(h_dep)
            v_box.addLayout(h_pa)
            
        v_box.addWidget(self.space)
        v_box.addWidget(self.calcul)
        self.setLayout(v_box)
        
        self.calcul.clicked.connect(self.affiche)
    
    def affiche(self):
        x0 = float(self.depart.text())
        pas = float(self.pas.text())
        prec = float(self.preci.text())
        L = [float(self.interval1.text()),float(self.interval2.text())]
        
        if self.min.isChecked():
            ext = 'min'
        elif self.max.isChecked():
            ext = 'max'
        
        if self.method == 'fixe':
            Question1_PasFixe.pasFixe(x0,pas,ext)
        elif self.method == 'accel':
            Question1_PasAccelere.pas_accelere(x0,pas,ext)
        else:
            Question1_Bissectrice.bissection(L,ext,prec)
            
class Q2(QWidget):

    def __init__(self):
        super().__init__()
        self.stylesheet = open('style.css').read()
        self.setStyleSheet(self.stylesheet)
        self.setWindowTitle('Question 1')
        self.l0 = QLabel("Vous calculez l'extremum de la fonction suivante : ")
        self.l3 = QLabel("X^3 -7*X^2 + 8*X - 3")
        self.l1 = QLabel('Point de départ : ')   
        self.depart = QLineEdit('5')
        self.l2 = QLabel('Précision : ')
        self.prec = QLineEdit('0.001')
        self.calcul = QPushButton('Calculer')
        self.calcul.setStyleSheet(self.stylesheet)
        self.space = QLabel()
        self.init_ui()
        
    def init_ui(self):
        v_box = QVBoxLayout()
        v_box.addWidget(self.l0)
        v_box.addWidget(self.l3)
        
        h1 = QHBoxLayout()
        h1.addWidget(self.l1)
        h1.addWidget(self.depart)
        v_box.addLayout(h1)
        
        h2 = QHBoxLayout()
        h2.addWidget(self.l2)
        h2.addWidget(self.prec)
        v_box.addLayout(h2)
        
        v_box.addWidget(self.space)
        v_box.addWidget(self.calcul)
        self.setLayout(v_box)
        
        self.calcul.clicked.connect(self.affiche)
        
    def affiche(self):
        x0 = float(self.depart.text())
        prec = float(self.prec.text())
        Question2_Newton_Raphson.NewtonRaphson(x0,prec)
        
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = Home()
    sys.exit(app.exec_()) 