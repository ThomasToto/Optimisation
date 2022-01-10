# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:18:45 2021

@author: Thomas
"""

from simplex_BigM import *

# Gestion inégalité/égalité ->  -1:'<=', 1:'>=', 0:'='





# Correction : https://www.youtube.com/watch?v=VZPn2CbTk20
'''print('\Exemple 1\n---------')
coeffFonction = [ 1.5,0.9 ]
coeffContrainte = [[1 ,0.5], [0.2, 0.15],[ 0, 1]]
resultat = [100, 25 ,160]
signe = [-1, -1, -1]
simple_BigM(coeffContrainte,resultat,coeffFonction,signe,'max')'''

# Correction : https://www.youtube.com/watch?v=zFdmXfpOEVc
print('\nExemple 1\n---------')
coeffFonction = [ 2,1 ]
coeffContrainte = [[2,1], [1,1]]
resultat = [8, 5]
signe = [-1, 1]
simplex_BigM(coeffContrainte,resultat,coeffFonction,signe,'max')
