def find_char(string, char):
    """Utilise la fonction enumerate qui, à chaque tour de boucle, fournie un indice et le caractère associé dans la chaîne 'string'.
    """
    for index, c in enumerate(string):
        if c == char:
            # le caractère est trouvé -> on renvoie son indice
            return index

    # la chaîne a été parcourue sans succès -> on renvoie -1
    return -1


print(find_char("Juliette & Roméo", "&"))  # renvoie 9

print(find_char("Juliette et Roméo", "&"))  # renvoie - 1
