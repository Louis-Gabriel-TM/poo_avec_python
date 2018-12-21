first_names = ['Jean-Michel', 'Marc', 'Vanessa',
               'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']

# Parcourons cette liste en affichant avec une chaîne formatée chaque prénom avec son nombre de caractrères
for name in first_names:
    print("Le prénom '{}' comporte {} caractères.".format(name, len(name)))
