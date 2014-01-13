#!/usr/bin/python2.7
# -*-coding:Utf-8 -*
from numpy import matrix
from matrice import *
INF = 9999 
#Définition des algo utilisés par le programme principal avec la matrice en argument

def floyd_algo(m):

	dim = m.getDimensions()
	
	# création d'une copie de la matrice passée en paramètre dans ta tableau tarbes.
	tabres = [[0 for x in xrange(dim)] for x in xrange(dim)] 

	for i in range (dim):
		for j in range(dim):
			tabres[i][j] = m.getValue(i,j);

	# parcours du tableau pour comparer chaque cas longueur d'un sommet à l'autre
	# et garder la valeur la plus petite.
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

###################Simplexe####################
def simplexe_algo(A, b, c, B, baseB, x_solution):
  nbLignes = A.shape[0]
  nbColonnes = A.shape[1]
  nbEtapes = 0
  A_ = A
  B_ = B
  b_= b
  z_ = sum([ c.A[0][i] * x_solution[i] for i in range(nbColonnes)])
  print "z_ initial: {0}".format(z_)

  

  A_ = B.I * A_
  Delta = simplexe_get_Delta(A_, c, baseB)
  
  while simplexe_has_Delta_negative_element(Delta):
    nbEtapes += 1
    print "\n\nEtape {0}:".format(nbEtapes)

    if nbEtapes > 1: A_ = B.I * A_
    print "A_: "
    print A_

    b_ = B.I * b_
    print "b_: "
    print b_
    
    B_ = simplexe_get_B_new(B_, A_, baseB)
  
    baseN = [ x for x in range(1, nbColonnes + 1) if x not in set(baseB)]

    s = simplexe_get_s(Delta)
    (r,Theta)  = simplexe_get_r_Theta(A_, b, baseB, s)
    x = simplexe_get_x(A_, Theta, b_, r, s, baseB, baseN)
    z_ = simplexe_get_z_new(z_, Delta, x, s)
    baseB = simplexe_get_baseB_new(baseB, r, s)
    Delta = simplexe_get_Delta(A_, c, baseB)
    print "\n"

  print "Solution finale: {0}, trouvee en {1} etapes.".format(x, nbEtapes)
  return x

def simplexe_get_Delta(A_, c, baseB):
  nbColonnes = A_.shape[1]
  Delta = []
  for j in range(nbColonnes):
    sum_delta = 0
    for i in baseB:
      sum_delta += c.A[0][i-1] * A_.A[i-1][j]
      #print "i: {0}, j: {1}, c[j]: {2}, A_[i][j]: {3}, sum_delta = {4}".format(i,j+1,c.A[0][j], A_.A[i-1][j], sum_delta)

    delta = c.A[0][j] - sum_delta
    #print "delta = {0}".format(delta)
    Delta.append(delta)
  
  print "Delta: {0}".format(Delta)
  
  return Delta

def simplexe_get_s(Delta):

  s = Delta.index(min(Delta)) + 1
  print "s: {0}".format(s)

  return s

def simplexe_get_r_Theta(A_, b_, baseB, s):
  min_a_determiner = []

  for i in baseB:
    if A_.A[i-1][s-1] > 0:
      min_a_determiner.append(b_.A[i-1][0] / A_.A[i-1][s-1])
  

  Theta = min(min_a_determiner)
  print "Theta: {0}".format(Theta)

  r = min_a_determiner.index(Theta) + 1
  print "r: {0}".format(r)

  return (r, Theta)

def simplexe_get_x(A_, Theta, b_, r, s, baseB, baseN):
  x = [None] * A_.shape[1]
  
  x[r-1] = 0
  x[s-1] = Theta

  for i in baseN:
    if i != r and i != s:
     x[i-1] = 0

  for i in baseB:
    if i != r and i != s:
      x[i-1] = b_.A[i-1][0] - A_.A[i-1][s-1] * Theta

  print "x: {0}".format(x)
  
  return x

def simplexe_get_z_new(z_old, Delta, x, s):
  z_new = z_old + Delta[s-1] * x[s-1]

  print "z_ new: {0}".format(z_new)

  return z_new

def simplexe_get_baseB_new(baseB_old, r, s):
  baseB_new = baseB_old[:]

  baseB_new[baseB_old.index(r)] = s
  
  print "baseB new: {0}".format(baseB_new)

  return baseB_new

def simplexe_get_B_new(B_, A_, baseB):
  for j in baseB:
    for i in range(B_.shape[0]):
      B_.A[i][baseB.index(j)] = A_.A[i][j-1]

  print "B_ new:"
  print B_

  return B_

def simplexe_has_Delta_negative_element(Delta):
  for i in Delta:
    if i < 0:
      return True

  return False
