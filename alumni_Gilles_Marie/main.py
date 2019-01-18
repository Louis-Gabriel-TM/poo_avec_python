import classes.user
import classes.databaseHandler
import classes.GUIhandler

db = classes.databaseHandler.myDatabaseHandler()
gui = classes.GUIhandler.myGUIhandler(db)
mdp = gui.display_login()
print (mdp)
gui.display_form()