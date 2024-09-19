# Bataille Navale

Ce projet est une version simplifiée du jeu de société classique "Bataille Navale", développée en Python en utilisant le module `turtle`. Le jeu se joue entre deux joueurs, chacun ayant une grille de bateaux placés aléatoirement. Les joueurs prennent des tours pour viser les bateaux de l'adversaire, et le jeu continue jusqu'à ce qu'un joueur coule tous les bateaux de l'autre.

## Fonctionnalités

- Chaque joueur possède une grille de 6x6 cases.
- Chaque joueur a 5 bateaux placés aléatoirement sur sa grille.
- Les joueurs prennent des tours pour viser une case de la grille de l'adversaire en entrant une coordonnée (ex : A2, B3).
- Les coups réussis sont marqués par un cercle rouge, tandis que les coups manqués sont marqués par une croix bleue.
- Le jeu se termine lorsqu'un joueur coule tous les bateaux de l'adversaire.

## Prérequis

- Python 3.x
- Module `turtle` (inclus avec Python standard)

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers source.
2. Assurez-vous d'avoir Python installé sur votre machine.
3. Aucune installation supplémentaire de dépendances n'est nécessaire, car `turtle` est inclus avec Python.

## Utilisation

Pour lancer le jeu, exécutez le script Python :

```bash
python touche_coule_[20227958].py
```

## Comment jouer

1. Le jeu démarre avec une grille pour chaque joueur : la grille du joueur 1 à gauche et celle du joueur 2 à droite.
2. Les joueurs prennent des tours pour viser une case de l'adversaire en entrant une coordonnée dans le format : Lettre (A-F) suivie d'un chiffre (1-6).
3. Si le tir touche un bateau, un cercle rouge apparaît sur la case visée. Sinon, une croix bleue est tracée.
4. Le jeu continue jusqu'à ce qu'un joueur coule tous les bateaux de l'adversaire.

## Auteur

- **Nom :** Johann Sourou

## Licence

© Avril 2023 - Johann Sourou. Tous droits réservés.

## Note

Ce projet a été développé à des fins éducatives et utilise `turtle` pour la visualisation graphique simple du jeu. Le code est optimisé pour fonctionner sur Codeboot uniquement.
