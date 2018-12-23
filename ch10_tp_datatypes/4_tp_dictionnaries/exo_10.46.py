def exchange_keys_values(dictionnary):
    """Cette fonction renvoie un dictionnaire 'result' où les couples clé / valeur du dictionnaire 'dictionnary' ont été renversés.
    """
    result = {}
    for key, value in dictionnary.items():
        result[value] = key
    return result


# Créons un petit dictionnaire anglais-français pour tester...
test_dict = {
    'computer': 'ordinateur',
    'keyboard': 'clavier',
    'mouse': 'souris'
}
print("Dictionnaire de départ >>>", test_dict)

# Et transformons-le en dictionnaire français-anglais
test_dict = exchange_keys_values(test_dict)
print("Dictionnaire renversé >>>", test_dict)
