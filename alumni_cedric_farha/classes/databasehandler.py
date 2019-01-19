import sqlite3


class DatabaseHandler:
    count = 0
    my_socket = None
    my_request = None

    def __init__(self):
        file = open("./databases/Database" + str(self.count) + ".sq3", "w")
        file.close()

        self.count += 1

    def connectDatabase(self, dbName):
            self.my_socket = sqlite3.connect(dbName)
            self.my_request = self.my_socket.cursor()

    def createDatabase(self):
        self.my_request.execute("""CREATE TABLE Students(
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            numero TEXT,
            voie TEXT,
            cp TEXT,
            ville TEXT,
            tel TEXT,
            mail TEXT,
            photo IMAGE
        )""")

    def setValues(self, surname, name, num='00000', lane='xxxxxxxxx', CP='00000', city='xxxxxx', port='0000000000', email='xxxxxxxxx', ph='ftygbk'):
        dataStudent = [[surname, name, num, lane, CP, city, port, email, ph]]

        for std in dataStudent:
            self.my_request.execute("""INSERT INTO Students (
            nom, prenom, numero, voie, cp, ville, tel, mail, photo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", std)

    def getValues(self):
        self.my_request.execute("SELECT * FROM Students")
        row = self.my_request.fetchone()

        while row is not None:
            print(row)
            row = self.my_request.fetchone()






if __name__ == "__main__":
    dbm = DatabaseHandler()
    dbm.connectDatabase("Database" + str(dbm.count) + ".sq3")

    dbm.createDatabase()

    dbm.setValues(surname="Dupond", name="Jean", CP="92250")
    dbm.setValues(surname="chouette", name="toto", city="Paris")


    dbm.getValues()
