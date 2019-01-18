def login():
    """
    Asks for the user password through GUI in order to login
    the database as either Student if password field is
    empty or Admin if "admin" is submitted

    otherwise loops till password equals "admin" or ""
    """

    pass


def navMenu():

    """
    Displays the navigation menu with all options available
    for the logged user:
        Student > Create/View
        Admin > All options from Student + Modify/Delete
    """

    pass


def displayForm():
    """
    Displays form. layout containing a student profile.
    Usable either in read only(view) or in rewritable
    (create/update) modes
    """
    pass


def createStudent():
    """
    Submits a student creation request to the database
    """
    pass


def viewStudent():
    """
    Submits a student profile view request to the database
    through use of a students list for student file selection.
    """
    pass


def updateStudent():
    """
    Submits a student profile update request to the database
    """
    pass


def deleteStudent():
    """
    Submits a student profile deletion request to the database.
    Warns before submission.
    """
    pass


def exit():
    """
    Commits all changes then exits the program
    """
    pass


if __name__ == "__main__":
    help(login)
