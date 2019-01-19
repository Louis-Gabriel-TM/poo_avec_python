import sqlite3

class myDatabaseHandler():
    def __init__(self):
        self.conn = sqlite3.connect('alumni.sq3')
        self.cur = self.conn.cursor()

        students = [
            # attributs 'name', 'lastname', number, 'street', zipcode, 'city'
            ['DRIDI', 'M.', 8, 'allee du Mas.', 77200, 'Champs'],
            ['MBOG', 'Marie', 22, 'impasse des droits', 75013, 'Paris'],
            ['PORIER', 'Nicolas', 1, 'rue du piedbot', 78010, 'Longchamps']
        ]

        # Creation de la base 
        try:
            self.cur.execute(
                """CREATE TABLE Students
                (name TEXT, lastname TEXT, 
                number INTEGER, street TEXT,
                zipcode INTEGER,
                city TEXT);"""
            )
            # insertion de données
            for student in students:
                self.cur.execute(
                    """INSERT INTO Students
                    (name, lastname, 
                    number, street,
                    zipcode,
                    city)
                    VALUES (?, ?, ?, ?, ?, ?);""", student
                )
        except sqlite3.OperationalError:
            # si l'exception est levée, c'est que la table est créée et il n'y a rien à faire de plus ici
            print("La table existe déjà !")
            pass
        pass
    def CREATE(self, liste):
        '''INSERT'''
        print("CREATE")
        # on utilise cette méthode contre les pirates
        for student in [liste]:
            self.cur.execute(
                """INSERT INTO Students
                (name, lastname, 
                number, street,
                zipcode,
                city)
                VALUES (?, ?, ?, ?, ?, ?);""", student
            )
        self.conn.commit()
        pass
    def READ(self):
        '''SELECT'''
        print("READ")
        self.cur.execute("SELECT * FROM Students")
        print(self.cur.fetchall())
        pass
    def UPDATE(self, liste):
        '''UPDATE'''
        print("UPDATE")
        # pour le WHERE il faut ajouter le name à la fin
        liste.append(liste[0])
        for student in [liste]:
            self.cur.execute(
                """UPDATE Students
                SET name = ?,
                    lastname = ?,
                    number = ?,
                    street = ?,
                    zipcode = ?,
                    city = ?
                WHERE name = ?;""", student
            )
        pass
    def DELETE(self, liste):
        '''DELETE'''
        print("DELETE")
        for student in [liste]:
            self.cur.execute(
                """DELETE FROM Students 
                WHERE name = ?;""", student
            )
        pass
    
    pass