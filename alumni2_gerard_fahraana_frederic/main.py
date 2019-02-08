import hashlib
#from tools.user import User
from tools.gui_handler import GuiHandler
from tools.data_base_handler import DbHandler



def button_connect_clicked():
    """ 
        Retrieve identifier and password from login page and call function
        verify_account. 
    """
    pass

#create the hashed password :
def hash_check():
    a = bytes(gui.shuttle[2],"utf-8")
    hashed_pwd = hashlib.sha256(a).hexdigest()
    return hashed_pwd

def verify_account():
    """ 
        Call the user class methode which retrieve all the identifier 
        registred in database and verify if its an existing account
        and if account is admin or student then call function admin_page 
        or student_page or guiHandler class methode which display error 
        message : account not found.
    """
    gui.shuttle[2] = hash_check()
    db.verify_user_account_exists(gui.shuttle)


def admin_page():
    """ Call the guiHandler class methode which display admin page and 
    retrieve the choice from create, read, update or delete profile then
    call User class methode create_profile, read_profile, update_profile
    or delete_profile and call the guiHandler class methode displaying 
    the correpsonding window or error message. """
    pass

def student_page():
    """ Call the guiHandler class methode which display student page and 
    retrieve the choice from create (his) , read, update (his)  or delete
    (his) profile then call User class methode create_profile, 
    read_profile, update_profile or delete_profile and call the guiHandler 
    class methode displaying the correpsonding window or error message. """
    pass

def button_quit_clicked():
    """ Call the guiHandler class methode which display the quit 
        program validation window. """
    pass

#def display_create_account():
    """ 
        When a student want to create an account, call the guiHandler 
        class methode which display the create user account page and
        retrieve the identifier and the 2 password entries and call the
        verify functions below then call function 
        button_validate_account_clicked or guiHandler class methode which
        display error message : error in creating account .
    """
#    pass

def verify_identifier():
    """ Check if identifier entry is empty. """
    pass
    

def verify_identifier_is_already_in_use():
    """ 
        Call the user class methode which retrieve list of identifiers 
        from database and check if identifier entry matches with 
        identifiers in list. 
    """
    pass

def verify_password_is_the_same():
    """ Check if password is the same in the two entries. """

def verify_password_format():
    """ 
        Check if password have at least 8 characters, one lowercase, 
        one capital letter and one figure. 
    """
    pass

def button_validate_account_clicked():
    """ 
        Call the methode which display validation page with accounts 
        informations and OK button then call create_user methode in 
        User class and call the guiHandler class methode which display
        the student menu.
    """
    pass

if __name__ == "__main__":
    """ Starting with welcome page. """
        
    gui = GuiHandler() # create guiHandler object
    db = DbHandler() # create DbHandler object
    
    
    gui.display_login() # call guiHandler class methode displaying 
                        # the welcome page
    
    if gui.shuttle[0] == "connection":
        verify_account()
        if db.shuttle[0] == 'account_accepted':
            gui.window.destroy()
            gui.display_user_menu()
            if gui.shuttle[0] == "students_list":
                db.read_students_list(gui.shuttle)
                gui.display_student_list()
        else :
            gui.error_msg("Ce compte n'existe pas")
    elif gui.shuttle[0] == "account_creation":
        gui.display_create_account()
        gui.shuttle[2] = hash_check()
        db.create_new_user(gui.shuttle)
        gui.display_user_menu()
    else:
        pass
        
    
    
    
    
    
    
    """
    
    user = User("ln", "fn", "ad", "pn", "em", "lbs", 
            "p", "el", "shuttle") # create user object with : last name, 
            # first name, adress, phone number, email adress, photo,  
            # estimated level in the different subjects and the shuttle


    """

