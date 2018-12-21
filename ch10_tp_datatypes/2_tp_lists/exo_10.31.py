# Prenons une liste de nombres désordonnée comportant des doublons
nb = [5, 3, 1, 5, 4, 4, 2, 3]

# Créons une liste vide qui recueillera les valeurs présentes dans la liste
values = []

for n in nb:  # Parcourons la liste initiale...
    if n not in values:  # ... et ajoutons chaque nombre dans 'values' uniquement s'il ne s'y trouve pas déjà
        values.append(n)

"""Il ne reste plus qu'à trier "en place" la liste 'values' avec la méthode 'sort()'.
Trier "en place" signifie que la liste est modifiée par ce tri.
On peut sinon créer une version triée de la liste, sans la modifier elle-même, avec la fonction 'sorted()'.
"""
values.sort()

print("Liste initiale >>>", nb)
print("Liste sans doublon et triée >>>", values)
