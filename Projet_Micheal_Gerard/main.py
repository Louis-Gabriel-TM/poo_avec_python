
from classes.user import User
from classes.guiHandler import Gui_handler
from classes.dbHandler import Db_Handler



if __name__ == "__main__":
    """ to start with welcome page """
    
    user1 = User("ln", "fn", "ad", "pn", "em", "lbs", "p", "")
    profil = user1.read_profile()

    gui1 = Gui_handler(profil)
    gui1.display_login()

    
