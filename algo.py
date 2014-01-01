#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from matrice import *
INF = 9999 
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


def BB(m):
	print "Branch & Bound"
	shorter = 0
	global shorterWay
	shorterWay = list() #= list()
	i = 0
	dim = m.getDimensions()
	# Attribution d'un chemin arbitraire
	for j in range(dim):
		shorter += m.getValue(i,(i+1)%dim)
		way = "[%d,%d]" % (i,(i+1)%dim)
		shorterWay.append(i)
		i = i + 1

	#parcours et recherche d'un chemin plus cours
	testWay = list()
	marqued = list()
	shorter = [INF]
	shorterWay = [list()]
	getShorterWay(m,marqued,shorter,shorterWay,0)

	print "Plus court %d " % (shorter[0])
	print shorterWay[0]

def getValuePath(path,m):
	res = 0
	for x in xrange(1,len(path)):
		res += m.getValue(path[x-1],path[x])
	return res

def getShorterWay(m,marqued,shorter,shorterWay,myShorter):
	dim = m.getDimensions()
	i = 0

	if (len(marqued) == 4):
		if(myShorter < shorter[0]):
			shorterWay[0] = marqued
			shorter[0] = myShorter

	for x in xrange(0,dim):
		if(not i in marqued):
			myMarqued = list(marqued)
			myMarqued.append(i)
			myShorter = getValuePath(myMarqued,m)
			if(myShorter < shorter[0]):
				getShorterWay(m,myMarqued,shorter,shorterWay,myShorter)
			else:
				break
		i += 1
	



#######################FIN###########################	

#############MPM#####################################
def mpm(m):
        
        dim = m.getDimensions()

        table = [[0 for x in xrange(dim)] for x in xrange(4)]
        #calcul des temps au plus tôt
        for i in range (dim):
                for j in range(dim):
                        if m.getValue(i,j) != 9999:
                                table[0][j]=max((table[0][i]+m.getValue(i,j)),table[0][j]);
        #calcul des temps au plus tard
        for i in range (dim):
                table[1][i]=9999;

        table[1][dim-1]= table[0][dim-1]

        for i in reversed(range(dim)):
                for j in reversed(range(dim)):
                        if m.getValue(j,i) != 9999:
                                table[1][j]=min(table[1][i]-m.getValue(j,i),9999) ;
        
        #calcul des marges libres
        for i in range(dim):
                table[2][i]=table[1][i]-table[0][i];                        
        
        print "Le chemin critique est :"

        for i in range(dim):
               if table[2][i]==0 :
                        print i ;
        res = Matrice(table)
        return res
        
#######################FIN###########################  	
