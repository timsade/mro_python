
class Matrice :
	def __init__(self,tab):
		self.data = tab
	
	def getValue(self, ligne, colonne):
		return self.data[ligne][colonne]
	
	def setValue(self, ligne, colonne, value):
		self.data[ligne][colonne] = value
	
	def getDimensions(self):
		j=0
		for i in range(len(data)):
			j+=1
	
		return i

	def getData(self):
		return self.data
