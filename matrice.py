#!/usr/bin/python2.7
# -*-coding:Utf-8 -*


######################################
###### Définition d'une matrice ######
######################################


class Matrice :
	
	# Initialisation
	def __init__(self,tab):
		self.data = tab
	
	# Retourne la valeur d'une case en fonctiion de la ligne et la colonne
	def getValue(self, ligne, colonne):
		return self.data[ligne][colonne]
	
	# Enregistre la valeur d'une case en fonction de la ligne et la colonne
	def setValue(self, ligne, colonne, value):
		self.data[ligne][colonne] = value
	
	# Retourne la dimension de la matrice
	def getDimensions(self):
		j=0
		for i in range(len(self.data)+1):
			j+=1
	
		return i

	# Retourne le nombre de colonne
	def getNbCol(self):
		k = 0
		for i in range(len(self.data[0])) :
			k+=1
		return k

	# Retourne la matrice
	def getData(self):
		return self.data

	# Affiche la matrice
	def affiche(self):
		res="	| ";

		for i in range(len(self.data[0])):
			res += str(i+1) + "	"
		res += '\n-------' 	

		for i in range(len(self.data[0])):
			res += "--------"
		res += '\n'

		i=1
		for el in self.data:
			res += "     "+str(i) +"	| "
			for  el2 in el:
				if el2 == 9999:
					res += "INF" + "	"
				else:					
					res += str(el2) + "	"
			res += "\n"
			i += 1
		return res

######################### FIN #########################