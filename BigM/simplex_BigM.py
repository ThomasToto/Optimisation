# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 10:05:17 2021

@author: Thomas
"""

import math, copy

def simplex_BigM(coeffContrainte,resultat,coeffFonction,signe,maxOuMin):

    # Affichage du problème
    affichageProbleme(coeffContrainte,resultat,coeffFonction,signe,maxOuMin)
    M=100
    (coeffContrainte,var,bas,pos)=tableau(coeffContrainte,resultat,coeffFonction, signe, maxOuMin,M)

    coeffContrainte=basePivot(coeffContrainte,pos)

    for k in range(0,10):
      index=indexPivot(coeffContrainte,bas,var)
      if index[0] > -1 and index[1] > -1:
        coeffContrainte=pivot(coeffContrainte,index)
        bas[index[0]-1]=var[index[1]-1]

    if verifErreur(coeffContrainte,M,var) == 0:
        print('Solution :')
        fonctionResultat(coeffContrainte,bas,len(coeffFonction),pos,maxOuMin)


def affichageProbleme(AA,bb,cc,signe,maxOuMin):
	coeffContrainte=copy.deepcopy(AA)
	resultat=copy.deepcopy(bb)
	coeffFonction=copy.deepcopy(cc)
	n = len(coeffFonction)
	m = len(resultat)


	# Function objective
	print(maxOuMin,' ',end='',sep='')
	for i in range(n):
		t= coeffFonction[i]
		if i > 0 :
			if t < 0:
				t=-1*t
				print(' - ',end='')
			else :
			    print(' + ',end='')
		elif t == -1:
			t=-1*t
			print('-',end='')
		if t == 1 :
			print(f'x{i+1}',end='')
		else:
			print(f'{t}x{i+1}',end='')

	# Contraintes
	print('\n','s.c.:',sep='',end='')

	for i in range(m):
		print('\n  ',end='')
		for j in range(n):
			t = coeffContrainte[i][j]
			if t == 0 :
				print('   ',end='')
			else:
				if j > 0 :
					if t < 0:
						t=-1*t
						print(' - ',end='')
					else :
						print(' + ',end='')
				elif t == -1:
					t=-1*t
					print('-',end='')
				if t == 1 :
					print(f'x{j+1}',end='')
				else:
					print(f'{t}x{j+1}',end='')
		if signe[i] == 1:
			print(' \u2265',resultat[i],end='')
		elif signe[i] == -1:
			print(' \u2264',resultat[i],end='')
		elif signe[i] == 0:
			print(' =',resultat[i],end='')


	# Contraintes sur les variables uniquement
	print('\n\n  ',end='')
	for i in range(n):
		print(f'x{i+1}',end='')
		if i < n-1 :
			print(',',end='')
	print(' \u2265 0\n')








def verifErreur(coeffContrainte,M,var):

    n=len(coeffContrainte[0])-1
    m=len(coeffContrainte)-1
    funb=0
    finf=0
    for j in range(n):
       if var[j][0:1] == 's' and coeffContrainte[m][j]  > 0 :
           funb =1
       elif var[j][0:1] == 's' and coeffContrainte[m][j]  <= -M :
           finf=1
    if funb : print('Erreur : problème non limité')
    if finf : print('Erreur : problème non faisable')
    return funb + finf







# Construction tableau
def tableau(AA,bb,cc, inq, pr, M):
    coeffContrainte=copy.deepcopy(AA)
    resultat=copy.deepcopy(bb)
    coeffFonction=copy.deepcopy(cc)
    ineqq=copy.deepcopy(inq)
    maxOuMin=copy.deepcopy(pr)

    #Listes des variables
    variables=[]
    base=[]
    posbase=[]
    n = len(coeffFonction)
    m = len(coeffContrainte)



    # Initialisation des variables

    for j in range(n):
        variables.append(f"x{j+1}")

    # Pour la minimisation
    coeffFonction = [x*-1 for x in coeffFonction]

    coeffFonction = copy.deepcopy(cc)
    coeffContrainte.append(coeffFonction)
    resultat.append(0)
    zero=[0.0]*len(resultat)
    naux=0
    nslack=0



    # Construction du tableau
    for i in range(0,len(ineqq)):
      coeffContrainte=ajoutColonne(coeffContrainte,zero)
      if ineqq[i] == 1:
          coeffContrainte[i][n+nslack+naux]=-1
          variables.append(f"s{nslack+1}")
          nslack +=1
          #bigM aux
          coeffContrainte=ajoutColonne(coeffContrainte,zero)
          coeffContrainte[i][n+nslack+naux]=1
          variables.append(f"coeffContrainte{naux+1}")
          base.append(f"coeffContrainte{naux+1}")
          coeffContrainte[m][n+nslack+naux]=-M
          naux +=1
      elif ineqq[i] == 0:
          coeffContrainte[i][n+nslack+naux]=1
          variables.append(f"coeffContrainte{naux+1}")
          base.append(f"coeffContrainte{naux+1}")
          coeffContrainte[m][n+nslack+naux]=-M
          naux +=1
      elif ineqq[i] == -1:
          variables.append(f"s{nslack+1}")
          base.append(f"s{nslack+1}")
          coeffContrainte[i][n+nslack+naux]=1
          nslack +=1
      posbase.append(n+nslack+naux)
    return (ajoutColonne(coeffContrainte,resultat),variables,base,posbase)






# Pivot de l'index +1 en une matrice des coeff des contraintes

def pivot(coeffContrainte, pivot_index):


        T=copy.deepcopy(coeffContrainte)
        i,j = pivot_index[0]-1,pivot_index[1]-1
        pivot = T[i][j]
        T[i] = [element / pivot for
                           element in T[i]]
        for index, row in enumerate(T):
           if index != i:
              row_scale = [y * T[index][j] for y in T[i]]

              T[index] = [x - y for x,y in zip(T[index],row_scale)]
        return T



# Fait des pivots consécutifs basés sur le vecteur col
def basePivot(T,V):
    coeffContrainte=copy.deepcopy(T)
    pos=copy.deepcopy(V)
    for k in range(0,len(pos)):
      coeffContrainte=pivot(coeffContrainte,[k+1,pos[k]])
    return coeffContrainte




# Evaluation des colonnes du simplex -> renvoie indexj

def pivotColonne(vv,vari):
    v=copy.deepcopy(vv)
    vmax=-1
    jmax=-2
    temp=vmax
    for j in range(0,len(v)-1):
      temp=v[j]
      if vari[j][0:1] != 'x':
         temp  = temp - 0.00009
      if temp > 0 and temp > vmax:
      	vmax = v[j]
      	jmax = j
    return jmax

# Evaluation des lignes du simplex -> renvoie indexi

def pivotLigne(vv,bb,basi):
	  v=copy.deepcopy(vv)
	  resultat=copy.deepcopy(bb)
	  vmin = 999999999.99
	  imin = -2
	  temp = vmin
	  for i in range(0,len(bb)-1):
	    if v[i] != 0 :
	       temp = resultat[i]/v[i]
	    if basi[i][0:1] == 's':
	       temp = temp - 0.009
	    if v[i] != 0 and temp > 0 and temp < vmin:
	  	    vmin = temp
	  	    imin = i
	  return imin


# Appel le calcul de l'index
def indexPivot(AA,basi,vari):
    coeffContrainte=copy.deepcopy(AA)

    indexj=pivotColonne(coeffContrainte[len(coeffContrainte)-1],vari)+1

    bb=vecteurColonne(coeffContrainte,len(coeffContrainte[0]))
    vv=vecteurColonne(coeffContrainte,indexj)
    indexi=pivotLigne(vv,bb,basi)+1
    return [indexi,indexj]




def ajoutColonne(matrice,vecteur):
    coeffContrainte=copy.deepcopy(matrice)
    resultat=copy.deepcopy(vecteur)
    for i in range(0, len(coeffContrainte)):
      # A la fin de la somme
      coeffContrainte[i] += [resultat[i]]
    return coeffContrainte


# Obtient un vecteur de la matrice des coefficients des contraintes
def vecteurColonne(coeffContrainte,colonne):
    coeffFonction=copy.deepcopy(colonne)
    coeffFonction-=1
    v=[]

    for i in range(0,len(coeffContrainte)):
    	v.append(coeffContrainte[i][coeffFonction])
    return v



# Pour afficher les coefficients des contraintes avec n décimales
def affichageDecimal(x):
	x = math.ceil(x*10000)/10000
	return x


# Crée une matrice identitée de n elements
def matriceIdentitee(n):
	MI = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
	return MI



# Crée une matrice avec que des zéros de n élements
def matriceZero(n):
    MI = [[0 for j in range(n)] for i in range(n)]
    return MI


# Affiche résultat final
def fonctionResultat(coeffContrainte,bas,n,pos,pr): 
    variables =[]
    valor=[]
    m=len(bas)  
    mA=len(coeffContrainte[0])-1 
    for k in range(n): 
     variables.append(f"x{k+1}")
     valor.append(0)
     
     # Pour chaque variable basique
     for i in range(m): 
       if variables[k] == bas[i]:
           valor[k] = coeffContrainte[i][mA]
     print(variables[k],valor[k])
    print('z',affichageDecimal(coeffContrainte[m][mA])*(-1 if pr=='max' else 1))


