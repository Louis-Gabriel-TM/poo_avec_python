long_str = """Ceci est une longue chaîne que nous devons découper en fragments de 5 caractères chacun pour les rassembler ensuite dans l'ordre inverse."""

# Dans la fonction 'print' le paramètre 'end' défini le caractère final. Par défaut, c'est un '\n' (pour 'new line' c'est-à-dire un saut de ligne) et ici ce sera deux sauts de lignes.
print("La longue chaîne :\n>>>", long_str, end='\n'*2)

# Découpons la chaîne en fragments de 5 caractères
fragments = []

while long_str:  # remarque : seule une chaîne vide est évaluée à False
    # ajoutons le fragment formé par les 5 premiers caractères
    fragments.append(long_str[:5])
    # gardons uniquement les caractères à partir du 6ème (indice = 5)
    long_str = long_str[5:]

print("Les fragments :\n>>>", fragments, end='\n'*2)

# Inversons l'ordre des fragments en parcourant cette liste à l'envers
fragments = fragments[::-1]
print("Les fragments en ordre inverse :\n>>>", fragments, end='\n'*2)

# Recollons les fragments dans une chaîne 'result'
result = "".join(fragments)
print("La longue châine modifiée :\n>>>", result, end='\n'*2)
