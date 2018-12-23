def set_people():
    """Cette fonction ajoute un élément au dictionnaire 'people'.
    Chaque élément du dictionnaire 'people' est donc un couple clé / valeur où la clé est 'name' et la valeur le tuple (age, height).
    Les variables 'name', 'age' et 'height' sont renseignées par l'utilisateur. Pour chacune d'entre-elles, une boucle vérifie que la variable est du bon type.
    """
    name = age = height = ""

    # pour 'name', on s'assure juste que la chaîne n'est pas vide
    while name == "":
        name = input("Entrez le nom de votre ami : ")

    # pour 'age', on essaye de convertir la 'string' entrée par l'utilisateur en un 'integer' avec un gestionnaire d'exception try / except
    while age == "":
        age = input("Entrez l'âge de votre ami : ")
        try:
            # on essaye de convertir la chaîne entrée
            age = int(age)
        except ValueError:
            # si la conversion lève l'exception TypeError, on réinitialise 'age' à "" pour faire un nouveau tour de boucle
            age = ""

    # pour 'height', c'est la même chose en essayant de convertir l'entrée en un 'float'
    while height == "":
        height = input("Entrez la taille de votre ami : ")
        try:
            height = float(height)
        except ValueError:
            height = ""

    # une fois les entrées validées, on les insère dans le dictionnaire 'people'
    people[name] = (age, height)


def get_people():
    """Cette fonction affiche les données correspondants à la clé 'name' au format 'Nom : <name> - âge : <age> ans - taille : <height> m
    """
    name = input("Quel est le nom de votre ami ? ")
    try:
        # on essaye de récupérer les données associées à la clé 'name'...
        age, height = people[name]
        print("Nom : {} - âge : {} ans - taille : {} m".format(
            name, age, height
        ))
    except KeyError:
        # ... et le try / except permet de gérer le cas où cette clé n'existe pas
        print("Cet ami ne se trouve pas dans le dictionnaire.")


people = {}
run = True
while run:
    print("1. Ajouter un ami")
    print("2. Consulter les informations sur un ami")
    print("3. Quitter")
    choice = input("Votre choix : ")
    if choice == "1":
        set_people()
    elif choice == "2":
        get_people()
    elif choice == "3":
        run = False
