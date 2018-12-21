"""La bibliothèque standard 'collections' contient de nouvelles structures de données qui peuvent s'avérer bien utiles.
On trouve sur le site Hackerrank une série de puzzles pour s'initier aux principales structures de données apportées par 'collections' :
https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-collections
"""
from collections import Counter


def count_char(string, char):
    """La variable 'occurences' est un 'Counter' dont les clés sont les caractères contenus dans la chaîne 'string' et les valeurs associées les occurences d'apparition de chaque caractère.
    Par exemple : Counter("Hello World!") renvoie Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, '!': 1})
    """
    occurences = Counter(string)
    return occurences[char]


print(count_char("ananas au jus", "a"))  # renvoie 4

print(count_char("Gédéon est déjà là", "é"))  # renvoie 3

print(count_char("Gédéon est déjà là", "z"))  # renvoie 0
