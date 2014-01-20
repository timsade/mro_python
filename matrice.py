#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

#Définition d'une matrice
class Matrice :
	
	def __init__(self,tab):
		self.data = tab
	
	def getValue(self, ligne, colonne):
		return self.data[ligne][colonne]
	
	def setValue(self, ligne, colonne, value):
		self.data[ligne][colonne] = value
	
	def getDimensions(self):
		j=0
		for i in range(len(self.data)+1):
			j+=1
	
		return i

	def getNbCol(self):
		k = 0
		for i in range(len(self.data[0])) :
			k+=1
		return k

	def getData(self):
		return self.data

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
