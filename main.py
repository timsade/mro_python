#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from matrice import *

print "------- MRO PYTHON ------ \n \
	1 - Programmation dynamique  \n \
	2 - Floyd-WHarshall\n \
	3 - Méthode des potentiels \n \
	4 - Ford-Fulkerson\n \
	5 - Procédures Branch et Bound \n \
	6 - Simplexe \n"
	
num = input()

def dyn():
	print "à faire"

def floyd():
	print "en cours"
	

algo ={	1 : dyn,
	2 : floyd
	#3 : poten,
	#4 : ford,
	#5 : branch,
	#6 : simplexe 
}

test = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]

m = Matrice(test)

algo[num]()



