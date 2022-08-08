# Le jeu du pierre feuille ciseau : La personne va choisir un élement entre les trois (pierre, feuille, ciseau)
# puis elle va valider son choix et l'ordinateur va donc choisir un des trois élements de manière aléatoire, puis
# l'ordinateur va lui renvoyer son choix et si elle a :
# pierre contre feuille elle perd
# feuille contre ciseau elle perd
# ciseau contre pierre elle perd
# sinon elle gagne
from random import *

# crée une liste d'options de jeu
options = ["Pierre", "Feuille", "Ciseaux"]

# Donne un nombre aléatoire au PC qui détérmine la place de "l'objet" qu'il va prendre (place numéro 0 = Pierre par exemple)
ordinateur = options[randint(0,2)]

# Met le joueur sur false de base (dès qu'il input une value il passe en true)
player = False

while player == False:
# Met le joueur sur vrai dès qu'il aura input une value
	player = input("Pierre, Feuille ou Ciseaux ?")
	if player == ordinateur:
		print("Egalité")
	elif player == "Pierre":
		if ordinateur == "Feuille":
			print("Dommage, tu as perdu ! (choix de l'ordinateur : " + ordinateur + ")")
		else:
			print("Bien joué, tu as gagné ! (choix de l'ordinateur : " + ordinateur + ")")
	elif player == "Ciseaux":
		if ordinateur == "Feuille":
			print("Bien joué, tu as gagné ! (choix de l'ordinateur : " + ordinateur + ")")
		else:
			print("Dommage, tu as perdu ! (choix de l'ordinateur : " + ordinateur + ")")
	elif player == "Feuille":
		if ordinateur == "Pierre":
			print("Bien joué, tu as gagné ! (choix de l'ordinateur : " + ordinateur + ")")
		else:
			print("Dommage, tu as perdu ! (choix de l'ordinateur : " + ordinateur + ")")

	else:
		print("Erreur, essaye de réecrir ton choix sans faire de faute et sans rajouter d'espace")

	player = input("La partie est finie, veux-tu rejouer ?")
	if player == "Oui" or player == "oui":
		player = False
		computer = options[randint(0, 2)]
	else:
		print("C'était cool, n'hésite pas à rejouer ;)")








