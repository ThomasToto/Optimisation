# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 19:01:40 2021

@author: Thomas
"""


def newton(fonctionCible,fonctionDerivee,x0,epsilon,MAX):
    '''Solution approximative de fonctionCible(x)=0 par la méthode de Newton.

    Paramètres
    ----------
    fonctionCible : Fonction
        Fonction pour laquelle nous cherchons une solution fonctionCible(x)=0.
    fonctionDerivee : Fonction
        Dérivée de fonctionCible(x).
    x0 : Nombre
        De telle sorte que fonctionCible(x)=0.
    epsilon : Nombre
        Condition d'arrêt tel que abs(fonctionCible(x)) < epsilon.
    MAX : Entier
        Nombre d'itération max

    Retour
    -------
    xn : Nombre
         Implémenter la méthode de Newton : calculer l'approximation linéaire
         de fonctionCible(x) en xn et trouver x via x = xn - fonctionCible(xn)/fonctionDérivé(xn)
         Continuer jusqu'à abs(fonctionCible(xn)) < epsilon puis renvoyer xn.
         Si fonctionDérivé(xn) == 0, retourne None. Si le nombre d'itérations
         dépasse MAX, puis return None.

    Exemples
    --------
    >>> fonctionCible = lambda x: x**2 - x - 1
    >>> fonctionDerivee = lambda x: 2*x - 1
    >>> newton(fonctionCible,fonctionDerivee,1,1e-8,10)
    Solution trouvée après 5 iterations.
    1.618033988749989
    '''
    xn = x0
    for n in range(0,MAX):
        fxn = fonctionCible(xn)
        if abs(fxn) < epsilon:
            print('Solution trouvée après',n,'iterations.')
            return xn
        Dfxn = fonctionDerivee(xn)
        if Dfxn == 0:
            print('Aucune dérivation. Aucune solution trouvée.')
            return None
        xn = xn - fxn/Dfxn
    print("Nombre d'itération max atteint. Aucune solution trouvée.")
    return None


'''
            MAIN
'''
#fonctionCible = lambda x: x**2 - x - 1
#fonctionDerivee = lambda x: 2*x - 1
#resultat = newton(fonctionCible,fonctionDerivee,1,1e-8,10)
#print(resultat)