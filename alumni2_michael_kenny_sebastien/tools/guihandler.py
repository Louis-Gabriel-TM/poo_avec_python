from tkinter import Tk, Label, LEFT, Entry, Button, BOTTOM, TOP, RIGHT


class GuiHandler:
    """ This class is the gui handler, for different views """

    def __init__(self):
        """ Send data to the main.py """

        self.shuttle = None

    def homepage(self):
        """ This class is for launching the first view """

        self.window = Tk()
        self.window.title("Page d'accueil")
        label = Label(self.window,
                      text='Entrer Login et Mot de passe : ',
                      fg='grey')
        label.pack(side=LEFT, padx=3, pady=3)
        self.login = Entry(self.window, bd=2)
        self.login.pack(side=LEFT)
        self.password = Entry(self.window, bd=2)
        self.password.pack(side=LEFT)
        send_btn = Button(self.window,
                          text="Entrer",
                          command=self.send_data)
        send_btn.pack(side=BOTTOM, padx=3, pady=3)
        self.window.mainloop()
        return self.shuttle

    def send_data(self):
        """ We send the data to the controller, in the main """
        self.shuttle = {}
        self.shuttle["login"] = self.login.get()
        self.shuttle["password"] = self.password.get()
        self.window.destroy()

    def page_admin(self):
        """ this class is for launching the admin view """
        self.window2 = Tk()
        self.window2.title("La Page Administrateur")
        label = Label(self.window2,
                      text='Selectionner : ', fg='grey')
        label.pack(side=TOP, padx=3, pady=3)

        CRF_btn2 = Button(self.window2,
                          text="CREATE_Fiche", command=self.create_file)
        CRF_btn2.pack(side=LEFT, padx=3, pady=3)

        LRF_btn3 = Button(self.window2,
                          text="READ_Fiche", command=self.read_file)
        LRF_btn3.pack(side=LEFT, padx=3, pady=3)

        MAJ_btn4 = Button(self.window2,
                          text="UPDATE_Fiche", command=self.update_file)
        MAJ_btn4.pack(side=LEFT, padx=3, pady=3)

        DLT_btn5 = Button(self.window2,
                          text="DEL_Fiche", command=self.delete_file)
        DLT_btn5.pack(side=LEFT, padx=3, pady=3)

        self.window2.mainloop()

    def create_file(self):
        """ We create the administration page """

        self.shuttle = "admin_create"
        self.window2.destroy()

    def read_file(self):
        """ For reading the administration page """

        self.shuttle = "admin_read"
        self.window2.destroy()

    def update_file(self):
        """ Here, we can update the different data in the database """

        self.shuttle = "admin_update"
        self.window2.destroy()
        return self.shuttle

    def delete_file(self):
        """ We can delete a profile """

        self.shuttle = "admin_delete"
        self.window2.destroy()
        return self.shuttle

    def show_create_file(self):
        """ this class is for launching the admin create file view """

        self.window3 = Tk()
        self.window3.title("Creation fiche etudiante")
        self.window3.geometry('750x650')

        label = Label(self.window3,
                      text='Remplir les champs \n '
                           'Pour être accepté, le MDP doit comporter \n\n'

                           '- au moins 8 caractères \n'
                           '- une minuscule \n'
                           '- une majuscule \n'
                           '- un chiffre \n',
                      fg='grey')

        label.pack(side=TOP, padx=3, pady=3)
        label2 = Label(self.window3,
                       text='Les Champs sont obligatoires ! ',
                       fg='grey')
        label2.pack(side=TOP, padx=3, pady=3)

        self.last_name_label = Label(self.window3,
                                     text='Nom',
                                     fg='grey',
                                     borderwidth=1)
        self.last_name_label.pack(side=TOP, padx=3, pady=3)
        self.last_name_entry = Entry(self.window3, bd=2)
        self.last_name_entry.pack(side=TOP, padx=3, pady=3)
        self.last_name_entry.insert(0, "Mageot")

        self.first_name_label = Label(self.window3,
                                      text='Prenom',
                                      fg='grey',
                                      borderwidth=1)
        self.first_name_label.pack(side=TOP, padx=3, pady=3)
        self.first_name_entry = Entry(self.window3, bd=2)
        self.first_name_entry.pack(side=TOP, padx=3, pady=3)
        self.first_name_entry.insert(0, "Michaël")

        self.phone_label = Label(self.window3,
                                 text='Telephone',
                                 fg='grey',
                                 borderwidth=1)
        self.phone_label.pack(side=TOP, padx=3, pady=3)
        self.phone_entry = Entry(self.window3, bd=2)
        self.phone_entry.pack(side=TOP, padx=3, pady=3)
        self.phone_entry.insert(0, "XX-XX-XX-XX-XX")

        self.mail_label = Label(self.window3,
                                text='Adresse Mail',
                                borderwidth=1)
        self.mail_label.pack(side=TOP, padx=3, pady=3)
        self.mail_entry = Entry(self.window3, bd=2)
        self.mail_entry.pack(side=TOP, padx=3, pady=3)
        self.mail_entry.insert(0, "xxxxxxxxx@xxxxx.xxx")

        self.adress_label = Label(self.window3,
                                  text='Adresse',
                                  fg='grey',
                                  borderwidth=1)
        self.adress_label.pack(side=TOP, padx=3, pady=3)

        self.number_label = Label(self.window3, text='Numero',
                                  fg='grey',
                                  borderwidth=1)
        self.number_label.pack(side=TOP, padx=3, pady=3)
        self.number_entry = Entry(self.window3, bd=2)
        self.number_entry.pack(side=TOP, padx=3, pady=3)
        self.number_entry.insert(0, "5")

        self.street_label = Label(self.window3,
                                  text='Voie',
                                  fg='grey',
                                  borderwidth=1)
        self.street_label.pack(side=TOP, padx=3, pady=3)
        self.street_entry = Entry(self.window3, bd=2)
        self.street_entry.pack(side=TOP, padx=3, pady=3)
        self.street_entry.insert(0, "Allée des fausse rouge")

        self.zip_code_label = Label(self.window3,
                                    text='Code Postal',
                                    fg='grey',
                                    borderwidth=1)
        self.zip_code_label.pack(side=TOP, padx=3, pady=3)
        self.zip_code_entry = Entry(self.window3, bd=2)
        self.zip_code_entry.pack(side=TOP, padx=3, pady=3)
        self.zip_code_entry.insert(0, "75222")

        self.city_label = Label(self.window3,
                                text='Ville',
                                fg='grey',
                                borderwidth=1)
        self.city_label.pack(side=TOP, padx=3, pady=3)
        self.city_entry = Entry(self.window3, bd=2)
        self.city_entry.pack(side=TOP, padx=3, pady=3)
        self.city_entry.insert(0, "Fontenay")

        back_btn7 = Button(self.window3,
                           text="Retour",
                           command=self.back_page_admin)
        back_btn7.pack(side=LEFT, padx=3, pady=3)

        validate_btn6 = Button(self.window3,
                               text="Valider",
                               command=self.check_form)
        validate_btn6.pack(side=RIGHT, padx=3, pady=3)

        self.window3.mainloop()

    def back_page_admin(self):
        self.shuttle = "back_page_admin"
        self.window3.destroy()

    def check_form(self):
        self.shuttle = "check_admin_form"

        self.shuttle2 = {}
        self.shuttle2["last_name_entry"] = self.last_name_entry.get()
        self.shuttle2["first_name_entry"] = self.first_name_entry.get()
        self.shuttle2["phone_entry"] = self.phone_entry.get()
        self.shuttle2["mail_entry"] = self.mail_entry.get()
        self.shuttle2["number_entry"] = self.number_entry.get()
        self.shuttle2["street_entry"] = self.street_entry.get()
        self.shuttle2["zip_code_entry"] = self.zip_code_entry.get()
        self.shuttle2["city_entry"] = self.city_entry.get()
        self.window3.destroy()

    def show_data(self, rows):
        self.window4 = Tk()
        self.window4.title("Affichage etudiant")
        for ligne in rows:
            label = Label(self.window4,
                          text=ligne,
                          fg='grey',
                          borderwidth=1)
            label.pack(side=TOP, padx=3, pady=3)

        self.window4.mainloop()
