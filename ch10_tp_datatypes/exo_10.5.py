def count_char(string, char):
    """La boucle 'for c in string:' donne pour valeur à la variable 'c' successivement tous les caractères de la chaîne 'string'.
    """
    occurences = 0
    for c in string:
        if c == char:  # si 'c' correspond au caractère recherché...
            occurences += 1  # ... on incrémente 'occurences'
    return occurences


print(count_char("ananas au jus", "a"))  # renvoie 4

print(count_char("Gédéon est déjà là", "é"))  # renvoie 3

print(count_char("Gédéon est déjà là", "z"))  # renvoie 0
