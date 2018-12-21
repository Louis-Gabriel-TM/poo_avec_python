"""
On peut également construire ces deux listes avec une particularité bien pratique de Python : les "compréhensions de listes".
Python permet en effet de générer directement une liste en la "décrivant".
"""
squares = [n * n for n in range(20, 41)]
cubes = [n * n * n for n in range(20, 41)]

print("Liste des carrés >>>", squares)
print("Liste des cubes >>>", cubes)

"""
Les compréhensions de listes (on devrait plutôt dire "listes en compréhension") sont un peu déroutantes au départ.
Mais elles permettent d'écrire un code plus condensé et, avec l'habitude, plus facile à comprendre.
"""
