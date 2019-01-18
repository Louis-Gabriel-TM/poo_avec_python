from classes.dbHandler import Db_Handler


class User:
    """ students class """

    def __init__(self, ln, fn, ad, pn, em, lbs, p, shuttle2):
        """ Constructeur """
        self.last_name = ln
        self.first_name = fn
        self.adress = ad
        self.phone_number = pn
        self.email = em
        self.level_by_subject = lbs
        self.photo = p
        
        self.shuttle2 = shuttle2

    def form_create(self):
        """ to add new student profile to database """
        pass

    def read_profile(self):
        """ to display a student profile from database """
        student = Db_Handler()
        self.shuttle2 = student.display_student()
        return self.shuttle2


    
class Admin(User):
    """ can do everything a user can do plus update and delete profile """

    def __init__(self, ln, fn, ad, pn, em, lbs, p, apwd = "admin"):
        User.__init__(self, ln, fn, ad, pn, em, lbs, p, apwd)
        self.admin_pwd = apwd

    def delete_profile(self):
        """ to remove a student profile from database """
        pass

    def update_profile(self):
        """ to modify profile in database """
        pass