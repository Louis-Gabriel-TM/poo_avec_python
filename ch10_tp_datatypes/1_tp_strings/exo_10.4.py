def find_char_2(string, char, start_index):
    """Utilise la fonction 'enumerate' qui, à chaque tour de boucle, fournie un indice et le caractère associé dans la chaîne 'string'.
    """
    for index, c in enumerate(string):
        # Il suffit de rajouter une condition index >= start_index
        if c == char and index >= start_index:
            return index

    return -1


print(find_char_2("César & Cléopâtre", "r", 5))  # renvoie 15

print(find_char_2("César & Cléopâtre", "s", 5))  # renvoie - 1
