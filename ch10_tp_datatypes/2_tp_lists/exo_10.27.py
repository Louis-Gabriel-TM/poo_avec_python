# Créons une liste vide pour les carrés et une autre pour les cubes
squares = []
cubes = []

# Utilisons la fonction 'range()' pour générer les entiers de 20 à 40
for n in range(20, 41):
    squares.append(n ** 2)
    cubes.append(n ** 3)
    # les exposants étant petits ici, il vaudrait mieux n'utiliser que des multiplications, pour accélérer ces calculs

print("Liste des carrés >>>", squares)
print("Liste des cubes >>>", cubes)
