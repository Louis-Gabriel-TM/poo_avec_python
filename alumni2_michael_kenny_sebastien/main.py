from tools.guihandler import GuiHandler
from tools.databasehandler import DatabaseHandler
from tools.adress import Adress
from tools.user import User
import re
import hashlib

""" Project by Sebastien, Micheal & Kenny
"""


def hash_password(password):
    """ We create a hash with sha256 hashing function for the password
    """

    m = hashlib.sha256()
    m.update(password.encode())
    m.digest()
    return m.hexdigest()


def check_password(login, password):
    """ Check input data from entry field
        To be accepted, a password must be :

        - at least 8 characters long
        - one lower case
        - one upper case
        - one digit long
    """

    if re.match(r'[A-Za-z0-9]{8,}', password):
        return True
    else:
        return False


def load_start_page_admin():
    """ The administrator's home page
        We display the authentication message
    """

    message = GUI.homepage()
    if message is not None:
        login = message["login"]
        password = message["password"]
        if check_admin(login, password):
            show_page_admin()
        elif check_user(login, password):
            page_user(login, password)
        else:
            load_start_page_admin()


def check_admin(login, password):
    """ Check if the password and login match
    """

    row = DBH.read_user_password(login)
    if row is not None:
        if hash_password(password) == row[1]:
            return True
        else:
            return False


def show_page_admin():
    """ We display the admin page with several options :
        Create, Read, Update, Delete
    """

    GUI.page_admin()
    response = GUI.shuttle
    if response == "admin_create":
        admin_create()
    elif response == "admin_read":
        admin_read()
    elif response == "admin_update":
        admin_update()
    elif response == "admin_delete":
        admin_delete()


def admin_create():
    """ Creation of the admin homepage
    """

    GUI.show_create_file()
    response = GUI.shuttle
    if response == "check_admin_form":
        check_admin_form()
    elif response == "back_page_admin":
        show_page_admin()


def check_admin_form():
    """ We create the form for the input datas
    """

    adress = Adress(GUI.shuttle2["number_entry"],
                    GUI.shuttle2["street_entry"],
                    GUI.shuttle2["zip_code_entry"],
                    GUI.shuttle2["city_entry"])

    user = User(GUI.shuttle2["last_name_entry"],
                GUI.shuttle2["first_name_entry"],

                adress,  # number, street, zip_code and city

                GUI.shuttle2["phone_entry"],
                GUI.shuttle2["mail_entry"], )

    DBH.create_user_profil_by_admin(user)


def admin_read():
    """ Read a student file
    """

    response = DBH.read_user_profil()
    GUI.show_data(response)


def admin_update():
    """ Update a student file
    """

    pass


def admin_delete():
    """ Delete a student file
    """

    pass


def check_user(login, password):
    pass


def page_user(login, password):
    pass


if __name__ == "__main__":
    DBH = DatabaseHandler()
    DBH.create_admin("Admin", hash_password("Admin42"))
    GUI = GuiHandler()
    load_start_page_admin()
