import turtle
import random
# Créer une fenêtre graphique
window = turtle.Screen()
window.title("Bataille naval")

# Créer une tortue
tortue = turtle.Turtle()




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

# Déclaration des imports et dépendances


# Déclaration des variables globales, constantes

espace_position_1 = 20 # de combien de pixel il faut s'éloigner afin de tracer la case juste à coté
decalage = 15 # valeur qui permet de déplacer les carrés et de différencier la première de la deuxième grille
taille_grille = 6
nb_de_bateau = 5

# Déclaration du code principal et Affichage

def fd(x):
    turtle.forward(x)
def rt(x):
    turtle.rt(x)
def pensize(x):
    turtle.pensize(x)
def pencolor(x,y,z):
    turtle.pencolor(x,y,z)
def pu():
    turtle.penup()
def pd():
    turtle.pendown()
def lt(x):
    turtle.left(x)
def goto(x,y):
    turtle.goto(x,y)
def goto(x,y):
    turtle.goto(x,y)
def clear():
    turtle.clear()
def afficher_alerte(x):
    print(x)


turtle.speed("fastest")


def croix(taille = 16, epaisseur = 2):
    pensize(epaisseur)
    pencolor(0.3,0.7,1)
    #croix
    for i in range(taille):
        fd(1); rt(90); fd(1); lt(90)
    pu()
    rt(180)
    for i in range(taille):
        rt(90); fd(1); lt(90); fd(1)
    rt(180)
    fd(taille)
    rt(180)
    pd()
    for i in range(taille):
        fd(1); lt(90); fd(1); rt(90)
    rt(90); pu(); fd(taille); pd(); rt(90)
    # carré
    for i in range(4):
        fd(taille), rt(90)

def cercle(taille = 0.15, epaisseur = 4):
    pencolor(1,0,0)
    pensize(epaisseur)
    pu(), fd(taille*53.5), pd()
    for i in range(360):
        fd(taille)
        rt(1)
    rt(180), pu(), fd(taille*53.5), pd(), rt(180)

def carre(taille = 16, epaisseur = 2):
    pensize(epaisseur)
    for i in range(4):
        fd(taille), rt(90)

# carre() trace des petits carrées utilisables plus tard pour générer la grille

def trace_un_carre(x,y,j = 1):
    global espace_position, decalage
    if j == 1 :
        decalage_in = -135
    else :
        decalage_in = decalage
    pencolor(0,0,0)
    pu(), goto(espace_position_1*x + (decalage_in),-espace_position_1*y + 60), pd()
    carre()

def trace_une_croix(x,y,j = 1):
    global espace_position, decalage
    if j == 1 :
        decalage_in = -135
    else :
        decalage_in = decalage
    pu(), goto(espace_position_1*x + (decalage_in),-espace_position_1*y + 60), pd()
    croix()

def trace_un_cercle(x,y,j = 1):
    global espace_position, decalage
    if j == 1 :
        decalage_in = -135
    else :
        decalage_in = decalage
    pu(), goto(espace_position_1*x + (decalage_in),-espace_position_1*y + 60), pd()
    cercle()

def convertir_en_coordonne(case = "A1"):
    case = case.upper()
    abcisse = case[0]
    ordonne = case[1]
    for i in range (6):
        if abcisse == "ABCDEF"[i] :
            abcisse = i+1
    for j in "123456" :
        if ordonne == j:
            ordonne = int(j)
    return (abcisse,ordonne)

def convertir_en_nom_de_case(x,y):
    abcisse = "ABCDEF"[x-1]
    ordonne = "123456"[y-1]
    return abcisse + ordonne

def generer_bateau():
    tab = []
    while len(tab) != 5 :
        x = int(25*(random.random()))+1
        if x in tab :
            continue
        else:
            tab += [x]
    return tab

def bateau_position(tab):
    position_bateau = []
    for i in tab :
        if i%5 == 0:
            abscisse = 5
        else:
            abscisse = i%5
        ordonne = (i + 4)//5
        position_bateau += [(abscisse,ordonne)]
    return position_bateau

#tab_1%5 # trouve la colonne donc l'abcisse de la case (horizontalement)
#(tab_1 + 4)//5 # trouve à quelle ligne se touve la case (verticalement)

tab_1 = bateau_position(generer_bateau())
tab_2 = bateau_position(generer_bateau())

def verifier_case(case):
    if len(case) == 0 :
        return False
    cond_1 = len(case) == 2 and case[1] in "123456"
    cond_2 = case[0] in "abcdef" or case[0] in "ABCDEF"
    valide = cond_1 and cond_2
    return valide

#Les données entrées par le joueur 2, sont enregistrés dans les tentatives dans la structure du joueur 1(et vice versa)

joueur_1 = {'bateau_j_1' : tab_1 , 'tentative_j_2' : [], 'compteur_1' : 0}
joueur_2 = {'bateau_j_2' : tab_2 , 'tentative_j_1' : [], 'compteur_2' : 0}

# demander_a_joueur_2(), demande une entré au joueur 2, (qui est verifier puis convertis en position (x,y))
# si l'entré appartient à la liste de bateau du joueur 2, un rond est tracé à la position entré
# sinon, une croix est tracé à cet même endroit
# demander_a_joueur_1(), fonctionne de la même manière

def barre_de_separation():
    pu(),goto(-18,95),pencolor(0,0,1),rt(90),pensize(10),pd(),fd(190),pencolor(0,0,0)

def retrace_grille_J1():
    k = 1
    for i in joueur_1['tentative_j_2']:
        if i in joueur_1['bateau_j_1'] :
            joueur_2['compteur_2'] += 1
    for i in range (6):
        for j in range (6):
            if (i+1,j+1) in joueur_1['tentative_j_2']:
                continue
            else :
                trace_un_carre(i,j,k)
    for i in joueur_1['tentative_j_2'] :
        if i in joueur_1['bateau_j_1'] :
            trace_un_cercle(i[0]-1,i[1]-1,k)
        else :
            trace_une_croix(i[0]-1,i[1]-1,k)

def retrace_grille_J2():
    k = 2
    for i in joueur_2['tentative_j_1'] :
        if i in joueur_2['bateau_j_2'] :
            joueur_1['compteur_1'] += 1
    for i in range (6):
        for j in range (6):
            if (i+1,j+1) in joueur_2['tentative_j_1']:
                continue
            else :
                trace_un_carre(i,j,k)
    for i in joueur_2['tentative_j_1'] :
        if i in joueur_2['bateau_j_2'] :
            trace_un_cercle(i[0]-1,i[1]-1,k)
        else :
            trace_une_croix(i[0]-1,i[1]-1,k)

def actualiser_affichage():
    clear()
    barre_de_separation()
    retrace_grille_J1()
    retrace_grille_J2()


def demander_a_joueur_2():
    k = 1
    tentative = input("JOUEUR 2 Entrer une case à visé chez JOUEUR 1")
    joueur_2['compteur_2'] = 0
    while not verifier_case(tentative):
        tentative = input("JOUEUR 2 Entrer une case à visé chez JOUEUR 1(de la forme A1 par exemple)")
    joueur_1['tentative_j_2'] += [convertir_en_coordonne(tentative)]
    actualiser_affichage()
    if convertir_en_coordonne(tentative) in joueur_1['bateau_j_1'] :
        print("Case", convertir_en_nom_de_case(convertir_en_coordonne(tentative)[0],convertir_en_coordonne(tentative)[1]), "du JOUEUR 1 :", "\nTouché !")
    else :
        print("Case", convertir_en_nom_de_case(convertir_en_coordonne(tentative)[0],convertir_en_coordonne(tentative)[1]),"du JOUEUR 1 :","\nRaté !")


def demander_a_joueur_1():
    k = 2
    tentative = input("JOUEUR 1 Entrer une case à visé chez JOUEUR 2")
    joueur_1['compteur_1'] = 0
    while not verifier_case(tentative):
        tentative = input("JOUEUR 1 Entrer une case à visé chez JOUEUR 2 (de la forme A1 par exemple)")
    joueur_2['tentative_j_1'] += [convertir_en_coordonne(tentative)]
    actualiser_affichage()
    if  convertir_en_coordonne(tentative) in joueur_2['bateau_j_2']:
        print("Case",convertir_en_nom_de_case(convertir_en_coordonne(tentative)[0],convertir_en_coordonne(tentative)[1]), "du JOUEUR 2 :", "\nTouché !")
    else :
        print("Case",convertir_en_nom_de_case(convertir_en_coordonne(tentative)[0],convertir_en_coordonne(tentative)[1]),"du JOUEUR 2 :","\nRaté !")


def jouer():
    print("TOUCHÉ-COULÉ")
    while True :
        demander_a_joueur_1()
        if joueur_1['compteur_1'] == 5 :
            afficher_alerte("Le JOUEUR 1 à gagner")
            break
        demander_a_joueur_2()
        if joueur_2['compteur_2'] == 5 :
            afficher_alerte("Le JOUEUR 2 à gagner")
            break

actualiser_affichage()
jouer()


window.exitonclick()