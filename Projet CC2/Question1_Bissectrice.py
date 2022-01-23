import pandas as pd


def suite(L,methode):
    x0 = (L[0]+L[1])/2
    x1 = (L[0]+x0)/2
    x2 = (x0+L[1])/2
    X = [x1,x0,x2]
    f0 = fonction(x0)
    f1 = fonction(x1)
    f2 = fonction(x2)
    F = [f1,f0,f2]
    if methode == 'min':
        if f1 == min(F):
            return [L[0],x0]
        elif f0 == min(F):
            return [x1,x2]
        else:
            return [x0,L[1]]

def fonction(X):
    return X**5 -5*X**3 -20*X +5


def bissection(L0,methode,e):
    if methode == 'min':
        m = 'minimum'
    else:
        m= 'maximum'
    MIN = [L0[0]]
    MAX = [L0[1]]
    L = list(L0)
    while (L[1]-L[0]) > (L0[1]-L0[0])*e:
        L = suite(L,methode)
        MIN.append(L[0])
        MAX.append(L[1])
    df = pd.DataFrame(list(zip(MIN,MAX)),columns=['min','max'])
    x_final = (L[0]+L[1])/2
    f_final = fonction(x_final)
    print(df)
    print(f'TLe {m} est {f_final} lorsque x = {x_final}')
