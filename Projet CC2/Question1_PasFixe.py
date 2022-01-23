import pandas as pd



def choix(x0,s,maxOuMin):
    minus = fonction_objective(x0-s)
    if maxOuMin == 'max':
        if minus < fonction_objective(x0):
            direction = '+'
        else:
            direction = '-'
    elif maxOuMin == 'min':
        if minus < fonction_objective(x0):
            direction = '-'
        else:
            direction = '+'
    return direction

def fonction_objective(X):
    return X**5 -5*X**3 -20*X +5

def suite(x,s,direction):
    if direction == '+':
        return x+s
    else:
        return x-s

def pasFixe(x0,s,maxOuMin):
    x = x0
    direction = choix(x0, s, maxOuMin)
    valeurX = []
    valeurFonction = []
    if maxOuMin == 'max':
        methode = 'maximum'
        while fonction_objective(suite(x,s,direction)) > fonction_objective(x):
            valeurX.append(x)
            valeurFonction.append(fonction_objective(x))
            x = suite(x,s,direction)
        valeurX.append(x)
        valeurFonction.append(fonction_objective(x))
        x = suite(x,s,direction)
        valeurX.append(x)
        valeurFonction.append(fonction_objective(x))
        i = valeurFonction.index(max(valeurFonction))
    elif maxOuMin == 'min':
        methode = 'minimum'
        while fonction_objective(suite(x,s,direction)) < fonction_objective(x):
            valeurX.append(x)
            valeurFonction.append(fonction_objective(x))
            x = suite(x,s,direction)
        valeurX.append(x)
        valeurFonction.append(fonction_objective(x))
        x = suite(x,s,direction)
        valeurX.append(x)
        valeurFonction.append(fonction_objective(x))
        i = valeurFonction.index(min(valeurFonction))
    df = pd.DataFrame(list(zip(valeurX,valeurFonction)),columns=['xi','f(xi)'])
    print(df)
    print(f'Résultat : le {methode} est {fonction_objective(valeurX[i])} lorsque x = {valeurX[i]}')
