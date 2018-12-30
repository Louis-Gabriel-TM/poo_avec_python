import sqlite3


# nom du fichier contenant la base de données SQLite
database = "music_db.sq3"

"""Les données à stocker dans la base de données 'music_db.sq3'
"""
composers = [
    # attributs 'name', 'birth_date', 'death_date'
    ["Mozart", 1756, 1791],
    ["Beethoven", 1770, 1827],
    ["Haendel", 1685, 1759]
]

opus = [
    # attributs 'composer', 'title', 'duration', 'player'
    ["Vivaldi", "Les quatre saisons", 20, "T. Pinnock"],
    ["Mozart", "Concerto pour piano No. 12", 25, "M. Perahia"],
    ["Brahms", "Concerto pour violon No. 2", 40, "A. Grumiaux"]
]

# création d'une connexion à la base de données
socket = sqlite3. connect(database)
# création d'un curseur qui contiendra les requêtes SQL à exéuter
request = socket.cursor()

"""On utilise un gestionnaire d'exception pour la création des tables de la bases de données.
En effet, si une table existe déjà, un exception 'OperationalError', interne à la bibliothèque 'sqlite3', est levée : il ne faudrait pas écraser une table déjà existante.
"""
# création de la table 'Composers'
try:
    request.execute(
        """CREATE TABLE Composers
        (name TEXT, birth_date INTEGER, death_date INTEGER)"""
    )
except sqlite3.OperationalError:
    # si l'exception est levée, c'est que la table est créée et il n'y a rien à faire de plus ici
    pass

# création de la table 'Opus'
try:
    request.execute(
        """CREATE TABLE Opus
        (composer TEXT, title TEXT, duration INTEGER, player TEXT)"""
    )
except sqlite3.OperationalError:
    pass

# insertion des données contenues dans la liste 'composers' dans la table 'Composers'
for composer in composers:
    request.execute(
        """INSERT INTO Composers
        (name, birth_date, death_date)
        VALUES (?, ?, ?)""", composer
    )

# insertion des données contenues dans la liste 'opus' dans la table 'Opus'
for op in opus:
    request.execute(
        """INSERT INTO Opus
        (composer, title, duration, player)
        VALUES (?, ?, ?, ?)""", op
    )

# récupérons et affichons les données de la table 'Composers' pour vérifier
request.execute("SELECT * FROM Composers")
print("Compositeurs >>>", list(request))

# même chose avec la table 'Opus'
request.execute("SELECT * FROM Opus")
print("Opus >>>", list(request))

""" Attention !!! La base de données n'est modifiée que si les opérations précédentes sont "commitées"
"""
socket.commit()

# fermeture du curseur
request.close()
# fin de la connexion à la base de données
socket.close()
