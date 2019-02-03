from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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


"""Création de la base de données et des classes 'Composer' et 'Opus' qui vont "mappées" les tables 'Composers' et 'Opus'
"""
Base = declarative_base()


class Composer(Base):
    __tablename__ = "Composers"
    uid = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Integer)
    death_date = Column(Integer)

    def __str__(self):
        return "{} ({} - {})".format(
            self.name, self.birth_date, self.death_date
        )


class Opus(Base):
    __tablename__ = "Opus"
    uid = Column(Integer, primary_key=True)
    composer = Column(String)
    title = Column(String)
    duration = Column(Integer)
    player = Column(String)

    def __str__(self):
        return "{}, de {}, interprété par {} (durée : {} min)".format(
            self.title, self.composer, self.player, self.duration
        )


# On créé / vide le fichier qui accueillera la base de données
f = open('example.db', 'w')
f.close()

# On définit la base de données et le SGBDR qui la gère (SQLite ici)
engine = create_engine('sqlite:///example.db')

# On créé les tables à partir des classes ci-dessus
Base.metadata.create_all(engine)

# On créé une session nous connectant à la base de données
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# On insère les données dans la table 'Composers' en créant des instances de la classe 'Composer'
for data in composers:
    new_composer = Composer(
        name=data[0],
        birth_date=data[1],
        death_date=data[2]
    )
    session.add(new_composer)

# Même chose pour la table 'Opus'
for data in opus:
    new_opus = Opus(
        composer=data[0],
        title=data[1],
        duration=data[2],
        player=data[3]
    )
    session.add(new_opus)

# On "commite" la session pour que ces modifications soient enregistrées
session.commit()

# On récupère et affiche les données de la table 'Composers' pour vérifier
print("\n<<< Compositeurs en base de données >>>")
request = session.query(Composer).all()
for composer in request:
    print(composer)

# Même chose avec les oeuvres
print("\n<<< Oeuvres en base de données >>>")
request = session.query(Opus).all()
for opus in request:
    print(opus)
