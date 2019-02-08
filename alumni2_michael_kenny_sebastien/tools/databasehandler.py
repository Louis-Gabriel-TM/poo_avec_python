import sqlite3


class DatabaseHandler:
    """ We crate the database handler for the communication between
        the controller and the database.
    """

    def __init__(self):
        """ The Database Constructor (three tables : adress, users, profils)
        """

        database = "database_student.sq3"  # The name of the database

        self.db1 = sqlite3.connect(database)
        self.request = self.db1.cursor()

        self.request.execute("""CREATE TABLE IF NOT EXISTS adress (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            number INTEGER,
            voie TEXT,
            post_code INTEGER,
            town TEXT NOT NULL
        )
         """)

        self.request.execute("""
        CREATE TABLE IF NOT EXISTS profils( 
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            last_name TEXT,
            first_name TEXT NOT NULL,
            mail TEXT NOT NULL,
            phone TEXT,
            number INTEGER,
            street TEXT,
            zip_code INTEGER,
            city TEXT,
            creator TEXT
        )
         """)

        self.request.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            login TEXT,
            password TEXT
        )
         """)
        self.db1.commit()  # save the data

    def create_admin(self, login, password):
        """ """
        self.request.execute(""" 
         INSERT INTO users(login, password) 
         VALUES('{}', '{}')
          """.format(login, password))

        self.db1.commit()
        self.request.execute(""" SELECT * FROM users """)
        row = self.request.fetchone()

    def create_user_profil_by_admin(self, user):
        """ We insert the user profil in the database with SQL
        """

        self.request.execute(
            "INSERT INTO profils("
            "last_name, "
            "first_name, "
            "mail, "
            "phone, "
            "number, "
            "street, "
            "zip_code, "
            "city, "
            "creator) "
            
            "VALUES(?,?,?,?,?,?,?,?,?)", 
            (user.last_name,
             user.first_name,
             user.mail,
             user.phone,
             user.adress.number,
             user.adress.street,
             user.adress.zip_code,
             user.adress.city, "create by admin"))
        
        self.db1.commit()

    def read_user_password(self, login):
        """ We read the the password user_profil from the table users
        """

        self.request.execute("""
        SELECT login, password FROM users WHERE login = '{}'
        """.format(login))

        row = self.request.fetchone()
        self.db1.commit()
        return row

    def read_user_profil(self):
        """ Read a profil
        """

        self.request.execute(""" SELECT * FROM profils """)
        rows = self.request.fetchall()
        return rows

    def update_user_profil(self):
        """ Update a profil
        """

        pass

    def delete_user_profil(self):
        """ Delete a profil
        """

        pass
