#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from matrice import *
from init import *
from algo import *


#le main qui ne fait qu'un switch case sur ce que l'utilisateur veut faire
while num != 0:

	print intro

	num = input("Entrer le numéro correspondant: ")
	print '\n'

	#début du switch case à la pyhton

	#dynamiques
	def dyn():
		print "à faire"

	def floyd():
		
		print "Matrice de test :"
		print floyd_cours.affiche()

		res = floyd_algo(floyd_cours) #appel de la fonction dans algo

		print "Résultat Algortihme Floyd-Warshall"
		print res.affiche()

	def johnson():
		print "Matrice de test :"
		print johnson_cours.affiche()

		res = johnson_algo(johnson_cours)

		print "Résultat Algortihme Johnson"
		ordre_pieces = "Ordre des pièces à fabriquer : "
		for elt in res:
			ordre_pieces += str(elt) + " "
		print ordre_pieces + '\n' 

	def exit():
		print "fin"
	

	algo ={	0 : exit,
		1 : dyn,
		2 : floyd,
		#3 : poten,
		4 : johnson
		#5 : ford,
		#6 : branch,
		#7 : simplexe
		
	}

	algo[num]() 






