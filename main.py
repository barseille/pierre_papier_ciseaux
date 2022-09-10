"""La méthode randint() génère un entier entre une plage donnée de nombres."""
from random import randint

"""Liste des options"""
jeu = ["pierre", "papier", "ciseaux"]

"""Attribuer une option aléatoire à l'ordinateur"""
ordinateur = jeu[randint(0, 2)]


print(ordinateur)

"""On initialise le décompte à zéro"""
pointsJoueur = 0
pointsOrdinateur = 0
continuer = True

"""La boucle continue jusqu'à ce que la variable continuer est fausse"""
while continuer:
    joueur = input("Choisissez entre PIERRE PAPIER CISEAUX ? ou tapez FIN pour arrêter !")

    """Scénarios"""
    if joueur == 'fin':
        continuer = False
    elif joueur == ordinateur:
        print("Egalité !")
        print(joueur, "contre", ordinateur)

    elif joueur == "pierre":
        if ordinateur == "papier":
            print("Perdu!")
            pointsOrdinateur = pointsOrdinateur + 1
            print(joueur, "contre", ordinateur)
        else:
            print("Gagné !")
            pointsJoueur = pointsJoueur + 1
            print(joueur, "contre", ordinateur)

    elif joueur == "papier":
        if ordinateur == "ciseaux":
            print("Perdu !")
            pointsOrdinateur = pointsOrdinateur + 1
            print(joueur, "contre", ordinateur)
        else:
            print("Gagné !")
            pointsJoueur = pointsJoueur + 1
            print(joueur, "contre", ordinateur)

    elif joueur == "ciseaux":
        if ordinateur == "pierre":
            print("Perdu !")
            pointsOrdinateur = pointsOrdinateur + 1
            print(joueur, "contre", ordinateur)
        else:
            print("Gagné!")
            pointsJoueur = pointsJoueur + 1
            print(joueur, "contre", ordinateur)


    else:
        print("Vérifier l'orthographe !")

    ordinateur = jeu[randint(0, 2)]

print("Joueur: ", pointsJoueur)
print("Ordinateur: ", pointsOrdinateur)

