# Commençons par importer la fonction 'sin()' et la constante pi de la bibliothèque standard 'math'
from math import pi, sin

# Implémentons une fonction convertissant les degrés en radians


def deg_to_rad(measure):
    return measure * 180 / pi


# Créons une liste vide pour recueillir les sinus
sinus = []

# Utilisons les 3 paramètres de 'range()' pour générer les entiers de 0 à 90 de 5 en 5 et ajouter à la liste chaque sinus correspondants
for angle_in_deg in range(0, 90, 5):
    angle_in_rad = deg_to_rad(angle_in_deg)
    sinus.append(sin(angle_in_rad))

print(sinus)
# Afficher la liste des sinus ici n'est pas très "parlant". Une boucle affichant chaque mesure et son sinus serait bienvenue...
