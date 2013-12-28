#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

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

	def getData(self):
		return self.data

	def affiche(self):
		res="";
		for el in self.data:
			for  el2 in el:
				if el2 == 9999:
					res += "INF" + " "
				else:					
					res += str(el2) + " "
			res += "\n"
		return res
