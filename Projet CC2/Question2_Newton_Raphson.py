import pandas as pd

def fonction(X):
    return X**3 -7*X**2 +8*X -3

def derivation1(X):
    return 3*X**2 -14*X +8

def derivation2(X):
    return 6*X - 14

def suite(X):
    return X - derivation1(X)/derivation2(X)

def NewtonRaphson(x,e):
    y = x
    L_x = [y]
    L_f1 = [abs(derivation1(y))]
    L_f = [fonction(y)]
    while abs(derivation1(y)) >= e:
        y = suite(y)
        L_x.append(y)
        L_f1.append(derivation1(y))
        L_f.append(fonction(y))
    df = pd.DataFrame(list(zip(L_x,L_f1,L_f)),columns=['xi',"|f'(xi)|",'f(xi)'])
    if L_f[len(L_f)-1] < L_f[len(L_f)-2]:
        methode = 'minimum'
    else:
        methode = 'maximum'
    print(df)
    print(f'Résultat : le {methode} est {L_f[len(L_f)-1]} lorsque x = {L_x[len(L_x)-1]}')
