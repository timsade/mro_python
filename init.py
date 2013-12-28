#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from matrice import *

#Initialisation des variables et des matrices utlisés en test 
#TODO matrice dans un fichier en lecture ? (pas ma priorité @timsade)

INF = 9999

intro = "------- MRO PYTHON ------ \n \
1 - Programmation dynamique  \n \
2 - Floyd-WHarshall\n \
3 - Méthode des potentiels \n \
4 - Ford-Fulkerson\n \
5 - Procédures Branch et Bound \n \
6 - Simplexe \n \
0 - Exit\n"

num=-10

tab_floyd_cours = \
	[[INF ,  3  ,  8  ,  6  , INF , INF ],\
	[ INF , INF , INF ,  2  ,  6  , INF ],\
	[ INF , INF , INF , INF ,  1  , INF ],\
	[ INF , INF ,  2  , INF , INF ,  7  ],\
	[ INF , INF , INF , INF , INF ,  2  ],\
	[ INF , INF , INF , INF , INF , INF ]]

tab_floyd_autre = \
	[[ 0  , 5   , INF , 10 ],\
	[ INF , 0   , 3   , INF],\
	[ INF , INF , 0   , 1  ],\
	[ INF , INF , INF , 0  ]]

floyd_cours = Matrice(tab_floyd_cours)
floyd_autre = Matrice(tab_floyd_autre)
