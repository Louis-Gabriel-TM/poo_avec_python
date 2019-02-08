import tools.user
import tools.databaseHandler
import tools.GUIhandler


db = tools.databaseHandler.myDatabaseHandler()
gui = tools.GUIhandler.myGUIhandler(db)
mdp = gui.display_login()
print (mdp)
gui.display_form()