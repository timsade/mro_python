#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from matrice import *

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
