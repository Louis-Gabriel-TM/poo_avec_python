def count_words(sentence):
    """On va commencer par éliminer tous les caractères qui ne sont ni des lettres, ni des chiffres, ni des espaces.
    """
    clean_chars = []  # Une liste pour recueillir lettres, chiffres et espaces

    for c in sentence:
        """La méthode 'isalnum()' teste si une chaîne ne contient que des lettres et des chiffres et renvoie un booléen (True / False).
        Elle est utilisée ici sur une chaîne 'c' qui se réduit à un seul caractère.
        """
        if c.isalnum() or c == " ":
            clean_chars.append(c)

    """On transforme la liste 'clean_chars' des caractères conservés en une chaîne avec la méthode 'join()'. Elle va accoler ici tous les caractères en plaçant un '' (c'est-à-dire rien) entre eux.
    """
    clean_sentence = ''.join(clean_chars)

    """On va utiliser maintenant la méthode 'split()'.
    Celle-ci découpe la chaîne en fonction du séparateur passé en argment (ici un espace mais il pourrait être omis car c'est le séparateur par défaut).
    Elle renvoie alors une liste contenant tous les fragments.
    """
    fragments = clean_sentence.split(" ")

    """Les fragments obtenus sont alors les mots de la phrase de départ.
    Il ne reste plus qu'à renvoyer le nombre de fragments
    """
    return len(fragments)


print(count_words(
    "Comptons les mots de cette première phrase."
))  # renvoie 7 et la phrase compte bien 7 mots

print(count_words(
    "Mais combien y-a-t-il de mots dans cette phrase ?"
))  # renvoie 9 alors que la phrase compte 11 mots...
