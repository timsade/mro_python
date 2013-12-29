#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from matrice import *

#Définition des algo utilisés par le programme principal avec la matrice en argument

def floyd_algo(m):

	dim = m.getDimensions()

	tabres = [[0 for x in xrange(dim)] for x in xrange(dim)] 

	for i in range (dim):
		for j in range(dim):
			tabres[i][j] = m.getValue(i,j);

	for k in range (dim):
		for i in range (dim):
			for j in range (dim):
				if tabres[i][k] + tabres[k][j] < tabres[i][j]:
					tabres[i][j] = tabres[i][k] + tabres[k][j];

	res = Matrice(tabres)
	return res

def johnson_algo(m):
	S = list();
	T = list();
	P =range(m.getDimensions());
	while P:
		rank = 0;
		mini = None;
		for i in P:
			newmin = min(m.getValue(i,0),m.getValue(i,1));
			if mini == None:
				mini =  newmin;
				rank = i;
			elif mini > newmin:
				mini = newmin;
				rank = i;
		if m.getValue(rank,0)<m.getValue(rank,1):
			S.append(rank+1);
		else:
			T.append(rank+1);
		P.remove(rank);
	T.reverse();
	return S + T;
	
#######################Ford-Fulkerson###########################

def fulkerson_algo(m,s,t,coupeMinimal):
	dim = m.getDimensions()
	tabres = [[0 for x in xrange(dim)] for x in xrange(dim)] 
	j=0
	sommetMarque=list()
	
	while marquer(m,tabres,s,t,INF,sommetMarque) != -1 : # tant qu'il y a un marquage
		sommetMarque = []
	for elt in sommetMarque: 
		coupeMinimal.append(elt) 
	res = Matrice(tabres)
	return res




def marquer(m,tabres,s,t,flot,sommetMarque):
	dim = m.getDimensions()	
	sommetMarque.append(s)	#les sommets déjà visités
	if(s==t): #si on est arrivé au puit(target)
		return flot
	nouveauFlot=0
	
	for j in range(dim): #marquage positif
		if(m.getValue(s,j)!=INF and (j not in sommetMarque) and tabres[s][j]<m.getValue(s,j)): 							
			flotPotentiel=m.getValue(s,j)-tabres[s][j]			
			nouveauFlot = marquer(m,tabres,j,t,min(flotPotentiel,flot),sommetMarque)
			if(nouveauFlot!=-1):
				tabres[s][j]+=nouveauFlot
				return nouveauFlot
	
	if(nouveauFlot==0 or nouveauFlot==-1):
		for j in range(dim):#marquage négatif
			if(m.getValue(j,s)!=INF and (j not in sommetMarque) and tabres[j][s]>0):
				flotPotentiel=tabres[j][s]
				nouveauFlot = marquer(m,tabres,j,t,min(flotPotentiel,flot),sommetMarque)
				if(nouveauFlot!=-1):
					tabres[j][s]-=nouveauFlot
					return nouveauFlot
	if(nouveauFlot==0 or nouveauFlot==-1):	#si il n'existe pas de successeur
		return -1


#######################FIN###########################		
