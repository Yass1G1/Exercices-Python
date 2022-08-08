# Le jeu est simple :
# l'ordinateur va choisir un nombre entre 1 et 10, et le joueur va essayer de le deviner en un certain nombre d'essais
# l'ordinateur va lui donner des indices comme notre nombre est trop bas/trop haut

import random

# Va sauvegarder le nom du joueur 
nom_joueur = input("Salut ! Entre ton nom pour commencer le jeu : ")

total_essais = input("En combien d'essais penses-tu arriver à deviner le nombre (maximum 15) ?")

def choix_essais():
	total_essais = input("En combien d'essais penses-tu arriver à deviner le nombre (maximum 15) ? (confirmation)")
	if int(total_essais) <= 5:
		print("Tu prefère le niveau le plus simple, petit joueur ;)")
		print("Okay " + nom_joueur + " essaye de deviner le nombre que j'ai choisi entre 1 et 10")
		jeu_facile()
	elif int(total_essais) > 10 <= 15:
		print("Enfait t'es un chaud tu prend le niveau maximum chakal")
		print("Okay " + nom_joueur + " essaye de deviner le nombre que j'ai choisi entre 1 et 30")
		jeu_difficile()
	elif int(total_essais) > 5 <= 10:
		print("tu as choisi le niveau moyen, courageux ;)")
		print("Okay " + nom_joueur + " essaye de deviner le nombre que j'ai choisi entre 1 et 20")
		jeu_moyen()

def restart():
	reponse = input("Veux tu refaire une partie (tu peux changer de niveau ;)) ?")
	if reponse == "Oui" or "oui":
		choix_essais()
	else:
		print("N'hésite pas à refaire une partie dès que tu en as l'envie !")
		quit()

def jeu_facile():
	nombre = random.randint(1, 10)
	nombre_essais = 0
	while nombre_essais <= 5:
		essais = int(input())
		nombre_essais += 1
		if essais == 0:
			nombre -= 1
			print("0 n'est pas entre 1 et 10 (cet essais ne compte pas ;) ).")
		if essais > nombre:
			print("Ton nombre est trop haut")
		if essais < nombre:
			print("Ton nombre est trop bas")
		if nombre_essais == 3:
			print("Attention il ne te reste que 2 essais")
		if nombre_essais == 4:
			print("Attention, c'est ton dernier essais")
		if nombre_essais == 5:
			print("Si tu as trouvé le bon nombre en 5 essais, tu as gagné, bravo ! Sinon tu à perdu et le nombre a trouver était : " + str(nombre) + " !")
			restart()
		if essais == nombre:
			print("Bravo, le nombre a trouver était :  " + str(nombre) + " !")
			restart()

def jeu_moyen():
	nombre = random.randint(1, 20)
	nombre_essais = 0
	while int(nombre_essais) <= int(total_essais):
		essais = int(input())
		nombre_essais += 1
		if essais == 0:
			nombre -= 1
			print("0 n'est pas entre 1 et 20 (cet essais ne compte pas ;) ).")
		if essais > nombre:
			print("Ton nombre est trop haut")
		if essais < nombre:
			print("Ton nombre est trop bas")
		if nombre_essais == int(total_essais) - 2:
			print("Attention il ne te reste que 2 essais")
		if nombre_essais == int(total_essais) - 1:
			print("Attention, c'est ton dernier essais")
		if nombre_essais == int(total_essais):
			print("Si tu as trouvé le bon nombre en " + total_essais + "essais, tu as gagné, bravo ! Sinon tu à perdu et le nombre a trouver était : " + str(nombre) + " !")
			restart()
		if essais == nombre:
			print("Bravo, le nombre a trouver était :  " + str(nombre) + " !")
			print("Bravo, le nombre a trouver était :  ", nombre, " !")
			print("Bravo, le nombre a trouver était :  {} !".format(nombre))
			restart()

def jeu_difficile():
	nombre = random.randint(1, 30)
	nombre_essais = 0
	while nombre_essais < 5:
		essais = int(input())
		nombre_essais += 1
		if essais == 0:
			nombre -= 1
			print("0 n'est pas entre 1 et 30 (cet essais ne compte pas ;) ).")
		if essais > nombre:
			print("Ton nombre est trop haut")
		if essais < nombre:
			print("Ton nombre est trop bas")
		if nombre_essais == int(total_essais) - 2:
			print("Attention il ne te reste que 2 essais")
		if nombre_essais == int(total_essais) - 1:
			print("Attention, c'est ton dernier essais")
		if nombre_essais == int(total_essais):
			print("Si tu as trouvé le bon nombre en 5 essais, tu as gagné, bravo ! Sinon tu à perdu et le nombre a trouver était : " + str(nombre) + " !")
			restart()
		if essais == nombre:
			print("Bravo, le nombre a trouver était :  " + str(nombre) + " !")
			restart()


choix_essais()
restart()

