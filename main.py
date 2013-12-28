#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from matrice import *
from init import *

m = Matrice(test)

while num != 0:

	print intro

	num = input("Entrer le numéro correspondant: ")
	print '\n'

	def dyn():
		print "à faire"

	def floyd():
		
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

		print "Résultat Algortihme Floyd-Warshall"
		res = Matrice(tabres)
		print res.affiche()
 

	def exit():
		print "fin"
	

	algo ={	0 : exit,
		1 : dyn,
		2 : floyd
		#3 : poten,
		#4 : johnson
		#5 : ford,
		#6 : branch,
		#7 : simplexe
		
	}

	algo[num]() 






