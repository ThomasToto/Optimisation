# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 16:20:01 2022

@author: Thomas
"""

def interval(n,pas,x1):
    
    if n>0:
        return x1+(n-1)*pas
    else:
        return x1+(n+1)*pas


def calcul(n,pas,x1):
    
    return interval(n,pas,x1)**2-1.5*interval(n,pas,x1)

def pasAccelere():
    
    pas=0.05
    n=1
    x1=0.0

    if calcul(2,pas,x1)>calcul(1,pas,x1):
        while calcul(n+1,pas,x1)>calcul(n,pas,x1):
            n-=1
            pas=2*pas
        interval1=interval(n-1,pas,x1)
        interval2=interval(n,pas,x1)
        
        
        
    if calcul(2,pas,x1)<calcul(1,pas,x1) :
        while calcul(n+1,pas,x1)<calcul(n,pas,x1):
            n+=1
            pas=2*pas
        interval1=interval(n-1,pas,x1)
        interval2=interval(n,pas,x1)

    elif calcul(2,pas,x1)>calcul(1,pas,x1) and calcul(2,pas,x1)>calcul(1,pas,x1):
        interval1=interval(-2,pas,x1)
        interval2=interval(2,pas,x1)
        
        
        
    elif calcul(2,pas,x1)==calcul(3,pas,x1):
        interval1=interval(1,pas,x1)
        interval2=interval(2,pas,x1)

    return n,interval1,interval2,pas

resultat=pasAccelere()
n = resultat[0]
interval1 = resultat[1]
interval2 = resultat[2]
pas = resultat[3]

print("Le point de minimum est entre ",interval1," et ",interval2)
