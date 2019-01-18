
import sqlite3

class Db_Handler:

    
    def __init__(self, dbname = "alumni_db.sq3"):
        self.dbname = dbname
        self.f = open(self.dbname, 'w')
        self.f.close()
        self.socket = sqlite3.connect(self.dbname)
        self.request = self.socket.cursor()

        self.create_student_table()
#        self.insert_for_test()

        self.request.execute("""INSERT INTO students ( first_name , last_name , adress , phone_number , email  , photo  , level_by_subject ) VALUES ("Michael","MAGEOT","la_planète_MARS","06-95-61-75-24","michaelmageaot@yahoo.fr","none","none")""")

        

    def create_student_table(self):
        try:
            self.request.execute(
                """ CREATE TABLE students (first_name ,last_name , adress , phone_number , email , photo , level_by_subject )
                 """
            )
        except sqlite3.OperationalError:
            pass

    def insert_for_test(self):
        """ tiny database création for 3 very spécial students :
        """
        self.request.execute("""INSERT INTO students ( first_name , last_name , adress , phone_number , email  , photo  , level_by_subject ) VALUES ("Michael","MAGEOT","la planète MARS","06-95-61-75-24","michaelmageaot@yahoo.fr","none","none")""")

        self.request.execute("""INSERT INTO students ( first_name , last_name , adress , phone_number , email  , photo  , level_by_subject ) VALUES ("Gérard","ALFANO","TORINO porta nuova","09-52-08-40-10","gege.alf@gmail.com","none","none")""")

        self.request.execute("""INSERT INTO students ( first_name , last_name , adress , phone_number , email  , photo  , level_by_subject ) VALUES ("Loic","MAGIN","Quelque part","00-00-00-00-00","nsp.nsp@nsp.com","none","none")""")


        

        self.socket.commit()

    def add_student(self):
        pass

    def delete_student(self):
        pass

    def display_student(self):
        self.request.execute("SELECT * FROM students")
        list_all = list(self.request)
        return list_all

if __name__ == "__main__":
    """ tiny database création for 3 students :
    """
    mabase = Db_Handler()
    
