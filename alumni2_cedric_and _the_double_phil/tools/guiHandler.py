import tkinter as tk
from tkinter import RIGHT
from .controller import Controller


class GUIHandler:
    def __init__(self):
        self.ctl = Controller(self)
        self.login_menu()

    def create_label(self, mst, txt, row, column, colspan=1):
        label = tk.Label(mst, text=txt, font=("Lucida Console", 16), justify=RIGHT)
        label.grid(row=row, column=column, columnspan=colspan)

        return label

    def create_button(self, mst, txt, cmd, row, column, colspan=1):
        bouton = tk.Button(mst, text=txt, command=cmd)
        bouton.grid(row=row, column=column, columnspan=colspan)

        return bouton

    def create_entry(self, mst, row, column, colspan=1, shw=""):
        field = tk.Entry(mst, show=shw)
        field.grid(row=row, column=column, columnspan=colspan)

        return field

    def logged_menu(self, mode, login):
        self.main_Window.destroy()

        self.logged_Window = tk.Tk()

        self.login_label2 = self.create_label(self.logged_Window, "Mode : " + login, 0, 0, 2)

        self.create_student_table_btn = self.create_button(self.logged_Window, "Creer Table Etudiant", self.ctl.create_table_request("student"), 2, 0)
        self.view_btn = self.create_button(self.logged_Window, "Consulter", self.ctl.view_request, 3, 0)
        self.insert_btn = self.create_button(self.logged_Window, "Inserer", self.ctl.insert_request, 4, 0)

        self.close_btn = self.create_button(self.logged_Window, "Fermer", lambda: [self.logged_Window.destroy(), self.login_menu()], 5, 0)
        self.exit_btn = self.create_button(self.logged_Window, "Quitter", lambda: [self.logged_Window.destroy(), self.ctl.db_shutdown_request()], 5, 1)

        self.logged_Window.mainloop()

    def view_result(self, results):
        self.result_Window = tk.Tk()

        self.title_label = self.create_label(self.result_Window, "Resultat", 0, 0)

        n = 2

        if len(results) == 0:
            self.create_label(self.result_Window, "Table vide", 2, 0)

        else:
            for elt in results:
                self.create_label(self.result_Window, elt, n, 0)
                n += 1

        self.return_btn = self.create_button(self.result_Window, "Retour", self.result_Window.destroy, n+2, 0)

        self.result_Window.mainloop()

    def login_menu(self):
        """
        Displays the login menu on apps launch
        """

        self.main_Window = tk.Tk()
        self.main_Window.configure(background="#4286F4")

        self.welcome_label = self.create_label(self.main_Window, "Bienvenue sur l'Appli Ce2Phil", 0, 0, 2)

        self.login_label = self.create_label(self.main_Window, "Pseudo : ", 2, 0)
        self.login_field = self.create_entry(self.main_Window, 2, 1)

        self.password_label = self.create_label(self.main_Window, "Mot de passe : ", 4, 0)
        self.password_field = self.create_entry(self.main_Window, 4, 1, shw="*")

        self.create_button(self.main_Window, "Creer un compte", self.display_form, 6, 0)
        self.create_button(self.main_Window, "Connexion", lambda: [self.ctl.login(self.login_field, self.password_field)], 6, 1)

        self.main_Window.mainloop()

    def display_form(self):
        self.main_Window.destroy()

        self.form_Window = tk.Tk()
        self.form_Window.configure(background="#4286F4")

        self.info_label = self.create_label(self.form_Window, "Creation de compte Ce2Phil", 0, 0, 2)

        # self.name_label = self.create_label(self.form_Window, "Nom : ", 2, 0)
        # self.name_field = self.create_entry(self.form_Window, 2, 1)
        #
        # self.forename_label = self.create_label(self.form_Window, "Prenom : ", 3, 0)
        # self.forename_field = self.create_entry(self.form_Window, 3, 1)
        #
        # self.number_label = self.create_label(self.form_Window, "Numero : ", 4, 0)
        # self.number_field = self.create_entry(self.form_Window, 4, 1)
        #
        # self.street_label = self.create_label(self.form_Window, "Voie : ", 5, 0)
        # self.street_field = self.create_entry(self.form_Window, 5, 1)
        #
        # self.zip_label = self.create_label(self.form_Window, "Code Postal : ", 6, 0)
        # self.zip_field = self.create_entry(self.form_Window, 6, 1)
        #
        # self.city_label = self.create_label(self.form_Window, "Ville : ", 7, 0)
        # self.city_field = self.create_entry(self.form_Window, 7, 1)
        #
        # self.tel_label = self.create_label(self.form_Window, "Telephone: ", 8, 0)
        # self.tel_field = self.create_entry(self.form_Window, 8, 1)
        #
        # self.email_label = self.create_label(self.form_Window, "Email : ", 9, 0)
        # self.email_field = self.create_entry(self.form_Window, 9, 1)
        #
        # self.avatar_label = self.create_label(self.form_Window, "Avatar : ", 10, 0)
        # self.avatar_field = self.create_entry(self.form_Window, 10, 1)
        #
        self.user_label = self.create_label(self.form_Window, "Pseudo : ", 2, 0)
        self.user_field = self.create_entry(self.form_Window, 2, 1)

        self.pwd_label = self.create_label(self.form_Window, "Mot de Passe : ", 3, 0)
        self.pwd_field = self.create_entry(self.form_Window, 3, 1, shw="*")

        self.confirm_pwd_label = self.create_label(self.form_Window, "Confirmer Mot de Passe : ", 4, 0)
        self.confirm_pwd_field = self.create_entry(self.form_Window, 4, 1, shw="*")

        self.return_btn = self.create_button(self.form_Window, "Retour", lambda: [self.form_Window.destroy(), self.login_menu()], 5, 0)
        self.create_button(self.form_Window, "Reinitialiser", self.ctl.form_clear, 5, 1)
        self.create_button(self.form_Window, "Envoyer", lambda: [self.form_Window.destroy(), self.ctl.submit(self.user_field.get(), self.pwd_field.get()), self.login_menu()], 5, 2)

        self.form_Window.mainloop()
