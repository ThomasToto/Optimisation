# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 13:56:23 2021

@author: Thomas
"""

# Initialisation des variables
pas=0.05
positionInit=0.0

def interval(n):
    if n>0:
        return positionInit+(n-1)*pas
    else:
        return positionInit+(n+1)*pas


def calcul(n):
    return interval(n)**2-1.5*interval(n)

def pasFixe():
    n=1
    if calcul(2)<calcul(1) :
        while calcul(n+1)<calcul(n):
            n+=1
        interval1=interval(n-1)
        interval2=interval(n)
    elif calcul(2)>calcul(1):
        while calcul(n+1)>calcul(n):
            n-=1
        interval1=interval(n-1)
        interval2=interval(n)
    elif calcul(2)==calcul(3):
        interval1=interval(1)
        interval2=interval(2)
    elif calcul(2)>calcul(1) and calcul(2)>calcul(1):
        interval1=interval(-2)
        interval2=interval(2)
    return n,interval1,interval2

resultat=pasFixe()
n=resultat[0]
interval1=resultat[1]
interval2=resultat[2]
print("Le point de minimum est entre ",interval1," et ",interval2,". Soit f(x*)=",calcul(n))
