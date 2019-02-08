import sqlite3


class myDatabaseHandler():
    def ecris_db_mdp(self, name0, mdp0): 
        # Requête SQL pour créer la table des MDPs            
        try:
            # insertion de données
            for mdp in [[name0, mdp0]]:
                self.cur.execute(
                    """INSERT INTO MDPs
                    (name, mdp)
                    VALUES (?, ?);""", mdp
                )
                print("WRITE_MDP")
            self.conn.commit()
        except sqlite3.OperationalError:
            # si l'exception est levée, c'est que la table est créée et il n'y a rien à faire de plus ici
            print("La table des MDPs existe-t-elle ?")
            pass

    def __init__(self):
        self.conn = sqlite3.connect('alumni.sq3')
        self.cur = self.conn.cursor()

        students = [
            # attributs 'name', 'lastname', number, 'street', zipcode, 'city', 'email', 'link_photo'
            ['DRIDI',       'M.',  8, 'allee du Mas.',      77200,     'Champs', 165000028, 'gd@club.fr',   'images/photoGD.jpg'],
            ['MBOG',     'Marie', 22, 'impasse des droits', 75013,      'Paris', 375730078, 'mm@orange.fr', 'images/photoMM.jpg'],
            ['PORIER', 'Nicolas',  1, 'rue du piedbot',     78010, 'Longchamps', 112345678, 'np@free.fr',   'images/photoNP.jpg']
        ]

        # On ne met que le mdp crypté de l'admin (les autres servent lors de tests)
        mdps = [
            ['admin', '847e768dc46a76e8fe4e36a66170a829']  #hashlib.md5(b"Admin42").hexdigest()],
            #['dridi', '01c2984c59be6d7ee30013fa12dd666a'],  #hashlib.md5(b"Drididridi42").hexdigest()],
            #['mbog', '6cbf24e94a6222ff1b02a40c1f047c10'],   #hashlib.md5(b"Mbogmbog42").hexdigest()],
            #['porier', 'e17d1e02501ace9575dcebc3a4271b4a']  #hashlib.md5(b"Porierporier42").hexdigest()]
        ]

        # Creation de la base
        # Requête SQL pour créer la table des MDPs            
        try:
            self.cur.execute(
                """CREATE TABLE MDPs
                (name VARCHAR(50), mdp INT
                );"""
            )
            # insertion de données
            for mdp in mdps:
                self.cur.execute(
                    """INSERT INTO MDPs
                    (name, mdp)
                    VALUES (?, ?);""", mdp
                )
            self.conn.commit()
        except sqlite3.OperationalError:
            # si l'exception est levée, c'est que la table est créée et il n'y a rien à faire de plus ici
            print("La table des MDPs existe déjà !")
            pass
        # Requête SQL pour créer la table des Etudiants            
        try:
            self.cur.execute(
                """CREATE TABLE Students
                (name VARCHAR(50), lastname VARCHAR(50), 
                number INTEGER, street VARCHAR(50),
                zipcode INTEGER,
                city VARCHAR(50),
                phone INTEGER,
                email VARCHAR(50),
                link_photo VARCHAR(256)
                );"""
            )
            # insertion de données
            for student in students:
                self.cur.execute(
                    """INSERT INTO Students
                    (name, lastname, 
                    number, street,
                    zipcode,
                    city,
                    phone,
                    email,
                    link_photo)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);""", student
                )
        except sqlite3.OperationalError:
            # si l'exception est levée, c'est que la table est créée et il n'y a rien à faire de plus ici
            print("La table des étudiants existe déjà !")
            pass
        pass

    def create(self, liste):
        '''INSERT'''
        print("CREATE")
        # on utilise cette méthode contre les pirates
        for student in [liste]:
            self.cur.execute(
                """INSERT INTO Students
                (name, lastname, 
                number, street,
                zipcode,
                city,
                phone,
                email,
                link_photo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);""", student
            )
        self.conn.commit()
        pass

    def read(self, ret=0):
        '''READ Students and return fetch if ret'''
        print("READ")
        self.cur.execute("SELECT * FROM Students")
        p = self.cur.fetchall()
        if ( ret ):
            return p
        else:
            print ( p )
        pass

    def readmdp(self):
        '''READ MotDePasse'''
        print("READMDP")
        self.cur.execute("SELECT * FROM MDPs")
        return self.cur.fetchall()

    def update(self, liste):
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
                    city = ?,
                    phone = ?,
                    email = ?,
                    link_photo = ?
                WHERE name = ?;""", student
            )
        self.conn.commit()
        pass

    def deletes(self, liste):
        '''DELETE'''
        print("DELETE")
        #self.cur.execute('begin')
        for student in [liste]:
            self.cur.execute(
                """DELETE FROM Students 
                WHERE name = ? AND city = ? AND email = ?;""", student
            )
            # On a pas réussi à faire fonctionner les transactions : BEGIN/END alors on bidouille
            self.cur.execute(
                """SELECT * FROM Students 
                WHERE name = ?;""", (student[0],)
            )
            l = len(self.cur.fetchall())   # récupère et efface les valeurs du curseurs, donc ne pas faire deux fois fetchall()
            print ( l )
            # efface le mot de passse si la ligne a disparu et on commit
            if l == 0:
                self.cur.execute(
                    """DELETE FROM MDPs 
                    WHERE name = ?;""", (student[0],)
                )
                self.conn.commit()
        pass
    pass