# Stockons les nombres premiers dans une liste
prime = [2, 3, 5, 7, 11, 13, 17, 19]

# Parcourons cette liste
for p in prime:
    # Affichons le début de la table de p
    for i in range(1, 16):
        print("{:5}".format(p * i), end="")
        # la sortie a été formatée pour prendre la place de 5 caractères dans tous les cas et de s'achever sans saut de ligne
    print()  # saut de ligne que l'on effectue une fois les 15 multiples affichés
