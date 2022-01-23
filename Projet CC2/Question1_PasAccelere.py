import pandas as pd



def choix(x0,s,minOuMax):
    minus = fonction(x0-s)
    if minOuMax == 'max':
        if minus < fonction(x0):
            direction = '+'
        else:
            direction = '-'
    elif minOuMax == 'min':
        if minus < fonction(x0):
            direction = '-'
        else:
            direction = '+'
    return direction

def fonction(X):
    return X**5 -5*X**3 -20*X +5

def nb(x0,s0,direction,i):
    if direction == '+':
        return x0+(s0*2**i)
    else:
        return x0-(s0*2**i)

def pas_accelere(x0,s0,minOuMax):
    i = 0
    x = x0
    valeurX = [x0]
    valeurFonction = [fonction(x0)]
    direction = choix(x0, s0, minOuMax)
    if minOuMax == 'max':
        methode = 'maximum'
        while fonction(nb(x0,s0,direction,i+1)) > fonction(nb(x0,s0,direction,i)):
            x = nb(x0,s0,direction,i+1)
            valeurX.append(x)
            valeurFonction.append(fonction(x))
            i+=1
    elif minOuMax == 'min':
        methode = 'minimum'
        while fonction(nb(x0,s0,direction,i+1)) < fonction(nb(x0,s0,direction,i)):
            x = nb(x0,s0,direction,i+1)
            valeurX.append(x)
            valeurFonction.append(fonction(x))
            i+=1
    df = pd.DataFrame(list(zip(valeurX,valeurFonction)),columns=['xi','f(xi)'])
    print(df)
    print(f'Résultat : le {methode} est {fonction(valeurX[len(valeurX)-1])} lorsque x = {valeurX[len(valeurX)-1]}')
