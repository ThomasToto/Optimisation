# -*- coding: utf-8 -*-
"""
Created on Thu Mon 20 11:37:11 2021

@author: Thomas
"""


import numpy as np
import matplotlib.pyplot as plt

# Définition fonction objective
def f(x):
    x1 = x[0]
    x2 = x[1]
    obj = x1**2 - 2.0 * x1 * x2 + 4 * x2**2
    return obj

# Définition gradiant objectif
def dfdx(x):
    x1 = x[0]
    x2 = x[1]
    grad = []
    grad.append(2.0 * x1 - 2.0 * x2)
    grad.append(-2.0 * x1 + 8.0 * x2)
    return grad

# Deuxième dérivée exacte (hessienne)
H = [[2.0, -2.0],[-2.0, 8.0]]

# Point départ
x_start = [-3.0, 2.0]

# Ligne servant d'échelle
i1 = np.arange(-4.0, 4.0, 0.1)
i2 = np.arange(-4.0, 4.0, 0.1)
x1_mesh, x2_mesh = np.meshgrid(i1, i2)
f_mesh = x1_mesh**2 - 2.0 * x1_mesh * x2_mesh + 4 * x2_mesh**2

# Création du plot
plt.figure()

# Contour de ligne
lines = range(2,52,2)


# Mise à jour de la figure avec les lignes servant d'échelle
CS = plt.contour(x1_mesh, x2_mesh, f_mesh,lines)

# Texte indicatif
plt.clabel(CS, inline=1, fontsize=10)

# Légende
plt.title('f(x) = x1^2 - 2*x1*x2 + 4*x2^2')
plt.xlabel('x1')
plt.ylabel('x2')


##################################################
# Méthode de Quasi-Newton 
##################################################


# Nombre d'itération
n = 8

# Utilise l'alphe pour chaque recherche
alpha = np.linspace(0.1,1.0,n)


# Initialisation de delta_xq et gamma
delta_xq = np.zeros((2,1))
gamma = np.zeros((2,1))
part1 = np.zeros((2,2))
part2 = np.zeros((2,2))
part3 = np.zeros((2,2))
part4 = np.zeros((2,2))
part5 = np.zeros((2,2))
part6 = np.zeros((2,1))
part7 = np.zeros((1,1))
part8 = np.zeros((2,2))
part9 = np.zeros((2,2))


# Initialisation de xq
xq = np.zeros((n+1,2))
xq[0] = x_start


# Initialisation du stockage de gradient 
g = np.zeros((n+1,2))
g[0] = dfdx(xq[0])


# Initialisation du stockage de l'hessienne
h = np.zeros((n+1,2,2))
h[0] = [[1, 0.0],[0.0, 1]]
for i in range(n):
    # Cherche la direction
    #  avec dx = -alpha * inv(h) * grad
    delta_xq = -np.dot(alpha[i],np.linalg.solve(h[i],g[i]))
    xq[i+1] = xq[i] + delta_xq

    # Mise à jour du gradient pour la prochaine étape  
    g[i+1] = dfdx(xq[i+1])

    # Mise à jour de l'hessienne pour la prochaine étape  
    gamma = g[i+1]-g[i]
    part1 = np.outer(gamma,gamma)
    part2 = np.outer(gamma,delta_xq)
    part3 = np.dot(np.linalg.pinv(part2),part1)

    part4 = np.outer(delta_xq,delta_xq)
    part5 = np.dot(h[i],part4)
    part6 = np.dot(part5,h[i])
    part7 = np.dot(delta_xq,h[i])
    part8 = np.dot(part7,delta_xq)
    part9 = np.dot(part6,1/part8)
    
    h[i+1] = h[i] + part3 - part9

plt.plot(xq[:,0],xq[:,1],'r-o')

# Sauvegarde l'image
plt.savefig('schema.png')

plt.show()
