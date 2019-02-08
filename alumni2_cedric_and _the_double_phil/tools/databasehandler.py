import sqlite3


class DatabaseHandler:
    def __init__(self, ctl_ref):
        self.ctl_ref = ctl_ref

        self.connector = sqlite3.connect("databases/database.sq3")
        # self.connector = sqlite3.connect("..//databases//database.sq3")
        self.request = self.connector.cursor()

        self.create_table("student")
        self.create_table("user")

    def db_shutdown(self):
        """
        Closes the cursor and connector to SQLite3 database
        """

        self.request.close()
        self.connector.close()

    def create_table(self, table):
        """
        Creates an initial empty table following "table" parameter :
            -> if table = user : Creates table User
            -> if table = student : Creates table Student
        """

        if table == "student":
            try:
                self.request.execute("""CREATE TABLE Student(
                    id              INTEGER     PRIMARY KEY     AUTOINCREMENT,
                    name            TEXT,
                    first_name      TEXT        NOT NULL,
                    number_way      INTEGER,
                    street          TEXT,
                    zip_code        INTEGER,
                    city            TEXT        NOT NULL,
                    num_tel         INTEGER,
                    mail            TEXT        NOT NULL,
                    creator_login   TEXT
                )""")

            except sqlite3.OperationalError:
                print("La table etudiant existe deja")

        elif table == "user":
            try:
                self.request.execute("""
                    CREATE TABLE User(
                        id          INTEGER     PRIMARY KEY     AUTOINCREMENT,
                        login       TEXT        NOT NULL,
                        password    TEXT        NOT NULL
                    )""")

            except sqlite3.OperationalError:
                print("La table utilisateur existe deja")

    def view_table(self, table):
        """
        Returns all table contents following "table" parameter :
            -> if table = user : Show table User content
            -> if table = student : Show table Student content
        """

        if table == "student":
            self.request.execute("SELECT * FROM Student")

        elif table == "user":
            self.request.execute("SELECT * FROM User")

        # print(self.request.fetchall())

        return self.request.fetchall()

        # row = self.request.fetchone()

        # while row is not None:
        #     print(row)
        #     row = self.request.fetchone()

    def view_profile(self, name, first_name):
        """
        View a specific student profile in table Student with "name" and
        "first_name" parameters
        """

        row = self.request.execute("SELECT * FROM Student WHERE name=(?) AND first_name=(?)", (name, first_name))

        while row is not None:
            print(row)
            row = self.request.fetchone()

    def view_user(self, login):
        """
        View a specific user in table User with "login" parameter
        """

        row = self.request.execute("SELECT * FROM User WHERE login=(?)", (login))

        while row is not None:
            print(row)
            row = self.request.fetchone()

    def get_profile(self, table, login, pwd):
        """
        Returns a tuple containing all table fields values to update table
        """

        profile = []

        if table == "student":
            profile_name = input("Entrer un nom : ")
            profile.append(profile_name)

            profile_first_name = input("Entrer un prenom : ")
            profile.append(profile_first_name)

            profile_number_way = input("Entrer un numero de rue : ")
            profile.append(profile_number_way)

            profile_street = input("Entrer un nom de rue : ")
            profile.append(profile_street)

            profile_zip_code = input("Entrer le code postal : ")
            profile.append(profile_zip_code)

            profile_city = input("Entrer le nom de la ville : ")
            profile.append(profile_city)

            profile_num_tel = input("Entrer un numero de telephone : ")
            profile.append(profile_num_tel)

            profile_mail = input("Entrer un mail : ")
            profile.append(profile_mail)

        elif table == "user":
            # user_login = input("Entrer un pseudo : ")
            profile.append(user_login)

            # user_password = input("Entrer un mot de passe : ")

            while not (len(user_password) > 8 and self.check_case(user_password)):
                # print("""Critere de format :
                #     -> Minimum 8 caracteres
                #     -> Au moins 1 minuscule
                #     -> Au moins 1 majuscule
                #     -> Au moins 1 chiffre""")

                user_password = input("Entrer un mot de passe : ")

            cipher_pwd = self.ctl_ref.generate_hash(user_password)
            profile.append(cipher_pwd)

        return tuple(profile)

    def check_case(self, pwd):
        """
        Checks if user password given in "pwd" parameter complies with
        the required format

        Required format :
            -> Min 8 characters long
            -> Min 1 upper case character
            -> Min 1 lower case character
        """

        count_upper = 0
        count_lower = 0

        for c in pwd:
            if c.isupper():
                count_upper += 1

            elif c.islower():
                count_lower += 1

        if (count_upper >= 1) and (count_lower >= 1):
            return True

        else:
            return False

    def insert_table(self, table, login, pwd):
        """
        Creates a profile in either Student or User tables specified
        in "table" parameter
        """

        if table == "student":
            profile = self.get_profile("student")

            self.request.execute("""
            INSERT INTO Student
            (
                name,
                first_name,
                number_way,
                street,
                zip_code,
                city,
                num_tel,
                mail
            )

            VALUES (?,?,?,?,?,?,?,?)""", profile)

        elif table == "user":
            profile = self.get_profile("user", login, pwd)

            self.request.execute("""
            INSERT INTO User
            (
                login,
                password
            )

            VALUES(?,?)""", profile)

        self.connector.commit()

    def update_table(self, table):
        """
        Updates an existing profile in either Student or User tables
        specified in "table" parameter
        """

        if table == "student":
            self.view_table("student")

            print()

            try:
                choice = int(input("Entrer l' ID de l etudiant a modifier : "))

            except(TypeError):
                print("Entree invalide")

            else:
                profile = self.get_profile("student")

                try:
                    self.request.execute("""
                        UPDATE Student SET
                            name = (?),
                            first_name = (?),
                            number_way = (?),
                            street = (?),
                            zip_code = (?),
                            city = (?),
                            num_tel = (?),
                            mail = (?)
                        """, profile)

                except(sqlite3.OperationalError):
                    print("Echec de la mise a jour")

                else:
                    print("Mise a jour OK")

        elif table == "user":
            self.view_table("user")

            print()

            try:
                choice = int(input("Entrer l' ID de l utilisateur a modifier : "))

            except(TypeError):
                print("Entree invalide")

            else:
                profile = self.get_profile("user")

                try:
                    self.request.execute("""
                        UPDATE User SET
                            login = (?),
                            password = (?)
                        """, profile)

                except(sqlite3.OperationalError):
                    print("Echec de la mise a jour")

                else:
                    print("Mise a jour OK")
                    self.request.commit()

    def delete_entry(self, table):
        """
        Deletes an entry in either Student or User tables specified in
        "table" parameter using the ID
        """

        if table == "student":
            self.view_table("student")

            print()

            try:
                choice = input("Entrer l' ID de l etudiant a supprimer : ")

            except(TypeError):
                print("Entree invalide")

            else:
                try:
                    self.request.execute("DELETE FROM Student WHERE id = (?)", choice)

                except(sqlite3.OperationalError):
                    print("Echec de la suppression")

                else:
                    print("Suppression OK")

        elif table == "user":
            self.view_table("user")

            print()

            try:
                choice = input("Entrer l' ID de l utilisateur a supprimer : ")

            except(TypeError):
                print("Entree invalide")

            else:
                try:
                    self.request.execute("DELETE FROM User WHERE id = (?)", choice)

                except(sqlite3.OperationalError):
                    print("Echec de la suppression")

                else:
                    print("Suppression OK")
                    self.connector.commit()



if __name__ == "__main__":
    mode = "user"

    db = DatabaseHandler()

    print("Create table...")
    db.create_table(mode)

    print("Insert table...")
    db.insert_table(mode)

    print("View table...")
    db.view_table(mode)

    # print("Update table...")
    # db.update_table(mode)

    # print("Delete entry...")
    # db.delete_entry(mode)

    print("Close connexion...")
    db.db_shutdown()
