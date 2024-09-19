import turtle
import random
###############################################################################
## Le programme suivant est une version simplifié du jeu bataille navale.
## Chaque joueur possède 5 bateaux répartit aléatoirement sur sa grille (La grille du joueur 1 est à gauche et celle du joueur 2 est à droite).
## Lorsque le jeux débute, le programme demande à chaque joueur alternativement de viser une case de l'adversaire (EX : A2, B3, E5 ...).
## le jeux se termine si un des joueurs arrive à détruire tous les bateaux du joueur adverse.
###############################################################################
## Auteur:  Johann Sourou (matricule : 20227958)
## Copyright: Copyright Avril 2023, touche_coule_[20227958].py
## Version: 1.0.0 (sur Codeboot uniquement)
## Date: 02 avril 2023
## Email: johann.sourou@umontreal.ca
###############################################################################

# Déclaration des variables globales, constantes

espace_position_1 = 20 # de combien de pixel il faut s'éloigner afin de tracer la case juste à coté
decalage = 15 # valeur qui permet de déplacer les carrés et de différencier la première de la deuxième grille
taille_grille = 6
nb_de_bateau = 5

# Déclaration des variables globales, constantes

espace_position_1 = 20  # de combien de pixels il faut s'éloigner afin de tracer la case juste à côté
decalage = 15  # valeur qui permet de déplacer les carrés et de différencier la première de la deuxième grille
taille_grille = 6
nb_de_bateau = 5

def afficher_alerte(message):
    print(message)

# Génère les bateaux aléatoirement
def generer_bateau():
    positions = set()
    while len(positions) < nb_de_bateau:
        x = random.randint(1, taille_grille)
        y = random.randint(1, taille_grille)
        positions.add((x, y))
    return list(positions)

# Vérifie si une case est valide
def verifier_case(case):
    if len(case) != 2:
        return False
    lettre, chiffre = case[0].upper(), case[1]
    return lettre in "ABCDEF" and chiffre in "123456"

# Convertit un nom de case (e.g., "A1") en coordonnées (x, y)
def convertir_en_coordonne(case="A1"):
    abcisse = "ABCDEF".index(case[0].upper()) + 1
    ordonne = int(case[1])
    return (abcisse, ordonne)

# Convertit des coordonnées en nom de case (e.g., (1, 1) -> "A1")
def convertir_en_nom_de_case(x, y):
    abcisse = "ABCDEF"[x - 1]
    ordonne = str(y)
    return abcisse + ordonne

# Affiche la grille de jeu
def afficher_grille(joueur, adversaire, joueur_num):
    print(f"\nGrille du Joueur {joueur_num} :")
    for y in range(1, taille_grille + 1):
        ligne = ""
        for x in range(1, taille_grille + 1):
            if (x, y) in joueur["tentatives"]:
                if (x, y) in adversaire["bateaux"]:
                    ligne += " O "  # Bateau touché
                else:
                    ligne += " X "  # Raté
            else:
                ligne += " . "  # Case vide
        print(ligne)

# Fonction pour demander au joueur de tirer
def demander_coup(joueur, adversaire, joueur_num):
    afficher_grille(joueur, adversaire, joueur_num)
    tentative = input(f"Joueur {joueur_num}, entrez une case à viser (ex: A1) : ")
    while not verifier_case(tentative):
        tentative = input(f"Joueur {joueur_num}, entrez une case valide (ex: A1) : ")
    coord = convertir_en_coordonne(tentative)
    if coord in joueur["tentatives"]:
        print("Vous avez déjà tiré sur cette case. Réessayez.")
        demander_coup(joueur, adversaire, joueur_num)
    else:
        joueur["tentatives"].append(coord)
        if coord in adversaire["bateaux"]:
            joueur["touches"] += 1
            print(f"Touché sur {tentative}!")
        else:
            print(f"Raté sur {tentative}.")

# Initialise le jeu
def jouer():
    joueur_1 = {"bateaux": generer_bateau(), "tentatives": [], "touches": 0}
    joueur_2 = {"bateaux": generer_bateau(), "tentatives": [], "touches": 0}
    
    print("TOUCHÉ-COULÉ : Le jeu commence !")
    while joueur_1["touches"] < nb_de_bateau and joueur_2["touches"] < nb_de_bateau:
        demander_coup(joueur_1, joueur_2, 1)
        if joueur_1["touches"] == nb_de_bateau:
            afficher_alerte("Le Joueur 1 a gagné!")
            break
        demander_coup(joueur_2, joueur_1, 2)
        if joueur_2["touches"] == nb_de_bateau:
            afficher_alerte("Le Joueur 2 a gagné!")
            break

# Lance le jeu
jouer()
