# Le jeu est simple :
# l'ordinateur va choisir un nombre entre 1 et 10, et le joueur va essayer de le deviner en un certain nombre d'essais
# l'ordinateur va lui donner des indices comme notre nombre est trop bas/trop haut

import random

# Va sauvegarder le nom du joueur 
nom_joueur = input("Salut ! Entre ton nom pour commencer le jeu : ")

print("Okay " + nom_joueur + " essaye de deviner le nombre que j'ai choisi entre 1 et 10")
def restart():
	reponse = input("Veux tu refaire une partie ?")
	if reponse == "Oui" or "oui":
		print("Okay " + nom_joueur + " essaye de deviner le nombre que j'ai choisi entre 1 et 10")
		jeu()
	else:
		print("N'hésite pas à refaire une partie dès que tu en as l'envie !")
		quit()

def jeu():
	nombre = random.randint(1, 10)
	nombre_essais = 0
	while nombre_essais < 5:
		essais = int(input())
		nombre_essais += 1
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
		if essais == nombre:
			print("Bravo, le nombre a trouver était :  " + str(nombre) + " !")
			restart()

jeu()
restart()





