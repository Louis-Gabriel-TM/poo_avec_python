import tkinter as tk


class GUIHandler:
    def __init__(self, dbHandler):
        self.loginMenu()

    def loginMenu(self):
        """
        Asks for the user password through GUI in order to login
        the database as either Student if password field is
        empty or Admin if "admin" is submitted

        otherwise loops till password equals "admin" or ""
        """

        self.mainWindow = tk.Tk()
        # self.mainWindow.geometry("600x300")
        # self.mainWindow.resizable(0, 0)

        self.labelLogIn = tk.Label(self.mainWindow, text="LOG IN")
        self.labelLogIn.grid()

        self.labelPassword = tk.Label(self.mainWindow, text="Enter password to log as ADMIN else directly click OK")
        self.labelPassword.grid()

        self.passwordField = tk.Entry(self.mainWindow)
        self.passwordField.grid()

        self.okButton = tk.Button(self.mainWindow, text="OK", command=self.getValue)
        self.okButton.grid()

        self.exitButton = tk.Button(self.mainWindow, text="EXIT", command=self.mainWindow.destroy)
        self.exitButton.grid()

        self.mainWindow.mainloop()

        # self.mainWindow = tk.Tk()
        # self.mainWindow.geometry("150x100")
        # self.mainWindow.resizable(0, 0)
        #
        # self.okButton = tk.Button(self.mainWindow, text="Student")  # , command=self.studentWindow)
        # self.okButton.grid()
        #
        # self.okButton = tk.Button(self.mainWindow, text="Admin", command=self.loginWindow)
        # self.okButton.grid()
        #
        # self.mainWindow.mainloop()

    def displayNavMenu(self, adminMode):
        """
        Displays the navigation menu with all options available
        for the logged user:
            Student > Create/View
            Admin > All options from Student + Modify/Delete
        """
        # Student Mode (empty password)
        if adminMode is False:
            self.menuWindow = tk.Tk()
            # self.menuWindow.geometry("900x600")
            # self.menuWindow.resizable(0, 0)

            self.labelUser = tk.Label(self.menuWindow, text="User")
            self.labelUser.grid()

            self.createButton = tk.Button(self.menuWindow, text="Create File", command=self.displayForm)
            self.createButton.grid()

            self.viewButton = tk.Button(self.menuWindow, text="View File")  # ,command=viewStudent)
            self.viewButton.grid()

            self.logoutButton = tk.Button(self.menuWindow, text="LOGOUT", command=lambda:[self.menuWindow.destroy(), self.loginMenu()])
            self.logoutButton.grid()

            self.exitButton = tk.Button(self.menuWindow, text="EXIT", command=self.menuWindow.destroy)
            self.exitButton.grid()

            self.menuWindow.mainloop()

        # Admin Mpde (password = admin)
        else:
            self.menuWindow = tk.Tk()
            # self.menuWindow.geometry("900x600")
            # self.menuWindow.resizable(0, 0)

            self.labelUser = tk.Label(self.menuWindow, text="ADMIN")
            self.labelUser.grid()

            self.createButton = tk.Button(self.menuWindow, text="Create File", command=self.displayForm)
            self.createButton.grid()

            self.viewButton = tk.Button(self.menuWindow, text="View File")  # ,command=viewStudent)
            self.viewButton.grid()

            self.editButton = tk.Button(self.menuWindow, text="Edit File")
            self.editButton.grid()

            self.logoutButton = tk.Button(self.menuWindow, text="LOGOUT", command=lambda:[self.menuWindow.destroy(), self.loginMenu()])
            self.logoutButton.grid()

            self.exitButton = tk.Button(self.menuWindow, text="EXIT", command=self.menuWindow.destroy)
            self.exitButton.grid()

            self.menuWindow.mainloop()

    def getValue(self):
        self.passwordValue = self.passwordField.get()
        self.mainWindow.destroy()

        if self.passwordValue == "admin":
            self.displayNavMenu(True)

        else:
            self.displayNavMenu(False)

    def getPassword(self):
        return self.passwordValue

    def displayForm(self):
        """
        Displays form. layout containing a student profile.
        Usable either in read only(view) or in rewritable
        (create/update) modes
        """

        self.formWindow = tk.Tk()

        self.labelName = tk.Label(self.formWindow, text="Name")
        self.labelName.grid()

        self.nameField = tk.Entry(self.formWindow)
        self.nameField.grid()


        self.labelSurname = tk.Label(self.formWindow, text="Surname")
        self.labelSurname.grid()

        self.surnameField = tk.Entry(self.formWindow)
        self.surnameField.grid()


        self.labelNumber = tk.Label(self.formWindow, text="Number")
        self.labelNumber.grid()

        self.numberField = tk.Entry(self.formWindow)
        self.numberField.grid()


        self.labelLane = tk.Label(self.formWindow, text="Lane")
        self.labelLane.grid()

        self.laneField = tk.Entry(self.formWindow)
        self.laneField.grid()


        self.labelPostalCode = tk.Label(self.formWindow, text="Postal Code")
        self.labelPostalCode.grid()

        self.postalCodeField = tk.Entry(self.formWindow)
        self.postalCodeField.grid()


        self.labelCity = tk.Label(self.formWindow, text="City")
        self.labelCity.grid()

        self.cityField = tk.Entry(self.formWindow)
        self.cityField.grid()


        self.labelTel = tk.Label(self.formWindow, text="Tel")
        self.labelTel.grid()

        self.telField = tk.Entry(self.formWindow)
        self.telField.grid()


        self.labelEmail = tk.Label(self.formWindow, text="Email")
        self.labelEmail.grid()

        self.emailField = tk.Entry(self.formWindow)
        self.emailField.grid()
