
import sqlite3

class DbHandler:
    def __init__ (self):
        self.shuttle = None
        # file containing the SQLite Database
        database = "alumni_db.sq3"
        # creating connection to the database
        self.socket = sqlite3.connect(database)
        #creating a cursor that will contain the SQL queries to execute
        self.request = self.socket.cursor()

    def verify_user_account_exists(self, shuttle):
        """ verify if the account with login and password entered is in database. """
        self.shuttle = shuttle
        self.request.execute(
            """SELECT count(*) FROM users 
               WHERE login = '{}' AND hash = '{}' """.format(self.shuttle[1],
               self.shuttle[2])
        )
        data = self.request.fetchone()[0]
        
        if data==0:
            self.shuttle[0] = "account_refused"
        else:
            self.shuttle[0] = "account_accepted"

        
    def create_new_user(self, shuttle):
        self.shuttle = shuttle
        self.request.execute(
            """INSERT INTO users (login, hash)
               VALUES ('{}', '{}')""".format(self.shuttle[1],
               self.shuttle[2])
        )
        self.socket.commit()


    def create_student_profile(self,shuttle):
        self.shuttle = shuttle
        self.request.execute(
            """INSERT INTO students (lastname, firstname, nbr, 
               street, zipcode, city, tel, mail, photo)
               VALUES ('{}', '{}','{}', '{}','{}', '{}','{}', '{}','{}')""".format(
                   self.shuttle[1],
                   self.shuttle[2],self.shuttle[3],self.shuttle[4],self.shuttle[5],
                   self.shuttle[6],self.shuttle[7],self.shuttle[8],self.shuttle[9])
        )
        self.socket.commit()

    def read_students_list(self, shuttle):
        self.shuttle = shuttle
        self.request.execute("""SELECT lastname, firstname FROM students order by lastname""")
        students_list = self.request.fetchall()
        self.shuttle = students_list

    def read_student_profile(self, shuttle):
        self.shuttle = shuttle
        self.request.execute("""SELECT * FROM students
        WHERE lastname = '{}' AND firstname = '{}'
        """.format(self.shuttle[0], self.shuttle[1])
        )
        profile = self.request.fetchall()
        self.shuttle = profile

