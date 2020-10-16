# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:59:38 2020

@author: Mathéo
"""
import requests

tous = "http://localhost:8080/tous"
affiche_produit = "http://localhost:8080/produit/"
ajouter_produit = "http://localhost:8080/ajouterunproduit/"

while True:
	choose = int(input("\n\nQue souhaitez-vous faire ?\n\n"
					   "1 - Afficher tous les produits ?\n"
					   "2 - Afficher un produit en fonction du code ?\n"
					   "3 - Ajouter un produit en fonction de l'id ?"))
	
	if choose == 1:
		resp = requests.get(tous)
		print(resp.text)
	elif choose == 2:
		id_produit = int(input("Veuillez saisir l'id du produit ?\n\n"))
		if id_produit > 0:
			resp = requests.get(affiche_produit + id_produit)
		else
			print("erreur : l'id doit être supérieur à 0")
	elif choose == 3:
		id_produit = int(input("Veuillez saisir l'id du produit à ajouter ?\n\n"))
		if id_produit > 0:
			resp = requests.get(ajouter_produit + id_produit)
		else
			print("erreur : l'id doit être supérieur à 0")









