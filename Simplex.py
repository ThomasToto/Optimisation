# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:24:05 2021

@author: Thomas
"""

class Contrainte():

    def __init__(self,nbSaisi,Variable):
        self.listeNomVar = []
        self.nbVar = nbSaisi
        self.listeVar = Variable
        self.nb_vari = len(self.listeVar)

        for k in range(self.nbVar):
            C = []
            for i in range(self.nb_vari):
                saisieMultiplicateur = input(f"Multiplicateur de {self.listeVar[i]} ?")
                C.append(int(saisieMultiplicateur))
            c = input("Comparé à : ")
            C.append(int(c))
            self.listeNomVar.append(C)

class Variable():

    def __init__(self,nbSaisi):
        self.listeNomVar = []
        self.nbVar = nbSaisi

        for i in range(self.nbVar):
            saisie = input(f'Nom de la variable {i+1} ?')
            self.listeNomVar.append(saisie)

class function():

    def __init__(self,Variable):
        self.listeNomVar = []
        self.listeVar = Variable
        self.nb_vari = len(Variable)

        for i in range(self.nb_vari):
            saisie = input(f"Multiplicateur de {self.listeVar[i]} ?")
            self.listeNomVar.append(int(saisie))


class tables():

    def __init__(self,vari,func,con):
        self.vari = vari.copy()
        self.nb_vari = len(vari)
        self.func = func
        self.con = con
        self.nb_con = len(con)
        self.table = []
        self.lines_taken = []
        self.pivot = []
        self.var = vari.copy()
        self.basi = [f'e{i}' for i in range(0,self.nb_con)]
        self.bas = self.basi.copy()

        L1 = [-1*k for k in self.func]
        L1.append(0)

        self.table.append(L1)
        for k in self.con:
            self.table.append(k)

        self.table[0].insert(len(self.table[0])-1,1)
        for k in range(self.nb_con):
            self.table[0].insert(self.nb_vari,0)

        for i in range(1,len(self.table)):
            self.table[i].insert(len(self.table[i])-1,0)
            for j in range(self.nb_vari,self.nb_vari+self.nb_con):
                if j-1 == i:
                    self.table[i].insert(j,1)
                else:
                   self.table[i].insert(j,0)

    def choose_pivot(self):
        index2 = self.table[0].index(min(self.table[0]))

        div1 = [None]
        div2 = [None]
        for i in range(1,len(self.table)):
            if self.table[i][index2] != 0:
                n = self.table[i][len(self.table[i])-1]/self.table[i][index2]
            else:
                n = None
            div1.append(n)
            if i not in self.lines_taken:
                div2.append(n)
        div3 = [i for i in div2 if i is not None]
        index1 = div1.index(min(div3))

        self.pivot = [index1,index2]

    def permute(self,i,j):
        M = []
        M.append(self.basi[i-1])
        if j < self.nb_vari:
            M.append(self.vari[j])
        else:
            M.append(self.basi[j-self.nb_vari])
        for k in range(len(self.vari)):
            if self.var[k] == M[0]:
                self.var[k] = M[1]
            elif self.var[k] == M[1]:
                self.var[k] = M[0]
        for k in range(len(self.basi)):
            if self.bas[k] == M[0]:
                self.bas[k] = M[1]
            elif self.bas[k] == M[1]:
                self.bas[k] = M[0]



    def transform(self):
        self.choose_pivot()
        i = self.pivot[0]
        j = self.pivot[1]
        nbSaisi = self.table[i][j]
        for k in range(len(self.table[i])):
            self.table[i][k] = self.table[i][k]/nbSaisi
        for l in range(len(self.table)):
            value = -1*self.table[l][j]
            if l == i:
                pass
            else:
                for m in range(len(self.table[l])):
                    self.table[l][m] = self.table[l][m] + value*self.table[i][m]
        self.lines_taken.append(i)
        self.permute(i,j)

    def loop(self):
        for i in range(self.nb_con):
            if min(self.table[0]) < 0:
                self.transform()


def proceed(nb_var,nb_con):
    vari = Variable(nb_var).listeNomVar
    func = function(vari).listeNomVar
    con = Contrainte(nb_con,vari).listeNomVar
    table1 = tables(vari,func,con)
    table1.loop()
    basi = [f'e{i}' for i in range(0,nb_con)]
    var = table1.var
    bas = table1.bas
    return vari, basi, var, bas, table1.table

def values(vari, basi, var, bas, T):
    Z = T[0][len(T[0])-1]
    R = len(vari)*[0]
    for i in range(len(vari)):
        if vari[i] not in bas:
            R[i] = 0
        else:
            j = bas.index(vari[i]) + 1
            R[i] = T[j][len(T[j])-1]
    return Z, R

def affiche(vari,Z,R):
    print()
    print("-----------------------------------------------")
    print("\033[4mResults\033[0m")
    print()
    print(f'Valeur maximale est F = {Z} avec :')
    for i in range(len(vari)):
        print(f'{vari[i]} = {R[i]}')

def simplex(nb_var,nb_con):
    vari, basi, var, bas, T = proceed(nb_var,nb_con)
    Z, R = values(vari, basi, var, bas, T)
    affiche(vari, Z, R)

nbVar = int(input("Nb de variable : "))
nbContrainte = int(input("Nb de contrainte : "))
simplex(nbVar,nbContrainte)
