
from tkinter import Button, Canvas, Tk, Label, Entry, Toplevel
from tkinter.messagebox import showinfo


class GuiHandler:
    def __init__ (self):
        self.shuttle = None
    
    def connection(self):
        """Deals with a clic on 'Connexion' button"""
        if not self.test_id():
            showinfo("Info", "Veuillez saisir un identifiant composé de caractères alphanumériques")
        elif not self.test_pw():
            showinfo("Info", "Veuillez saisir un mot de passe")
        else:
            self.shuttle = ["connection", self.uid.get(), self.pw.get()]
            self.window.quit()

    def test_id(self):
        """test if user id is alphanumeric"""
        return self.uid.get().isalnum()

    def test_pw(self):
        """test if password is not nul"""
        return self.pw.get() != ""

    def account_creation(self):
        """Deals with a clic on 'Création de compte' button on the connection window"""
        self.shuttle = ["account_creation"]
        self.window.destroy()

    def quit(self):
        """closes connection window"""
        self.shuttle = ["quit"]
        self.window.quit()

    def error_msg(self, msg):
        showinfo("Info", msg)

    
    def sans_objet(self):
        pass




####################################################################
####    "CONNECTION" BOX                                        ####
####################################################################
    def display_login(self):
        """ Creation of welcome/connection page """

        # creation of window 
        self.window = Tk()
        self.window.title('Page d\'acceuil')

        # ID
        label_Id = Label(self.window, text="Identifiant :")
        self.uid = Entry(self.window, width=30)
        label_Id.grid(row=1,column=1)
        self.uid.grid(row=1,column=2)

        # Pwd
        label_pw = Label (self.window, text="Mot de passe :")
        self.pw = Entry (self.window, width=30, show='*')
        label_pw.grid(row=2,column=1)
        self.pw.grid(row=2,column=2)

        #Line feed
        sdl = Label (self.window, text="")
        sdl.grid(row=3,column=2)

        # button 'Connexion'
        btnCnx = Button(self.window, text="Connexion", command=self.connection)
        btnCnx.grid(row=4,column=1)

        # button 'Créer un compte'
        btnCpt = Button(
            self.window, 
            text="Créer un compte", 
            command=self.account_creation
            )
        btnCpt.grid(row=4,column=2)

        #close window button
        btnQuit = Button(self.window, text="Quitter", command=self.quit)
        btnQuit.grid(row=4,column=3)

        # window launch
        self.window.mainloop()


#############################################################################


    def validate_account_creation(self):
        """Deals with a clic on 'Valider' button of create account window"""
        digs = "0123456789"
        speci = "\"'#"
        if not self.test_id():
            showinfo("Info", "Veuillez saisir un identifiant composé de caractères alphanumériques")
        elif self.uid.get() == 'admin':
            showinfo("Info", "L'identifiant ne peut pas être 'admin'")
        elif self.pwd1.get() != self.pwd2.get():
            showinfo("Info", "Le mot de passe doit être saisi et identique dans les deux champs")
        elif len(self.pwd1.get()) < 8 or \
            self.pwd1.get() == self.pwd1.get().upper() or \
            self.pwd1.get() == self.pwd1.get().lower() or \
            not set(self.pwd1.get()) & set(digs) or \
            set(self.pwd1.get()) & set(speci) :
            showinfo("Info",
                """Le mot de passe doit vérifier les conditions suivantes :
                - longueur supérieure à 7 caractères ;
                - contient au moins une minuscule, une majuscule et un chiffre ;
                - ne contient pas l'un de ces 3 caractères spéciaux :  "  ' #"""
                )
        else:
            self.shuttle = ["account_creation", self.uid.get(), self.pwd1.get()]
            self.create_account_window.quit()





####################################################################
####    "CREATE ACCOUNT" BOX                                    ####
####################################################################

    def display_create_account(self):
        """ Creation of "create account" window """

        self.create_account_window = Tk()
        self.create_account_window.title('Création d\'un compte utilisateur')

        # ID field
        label_Id = Label (self.create_account_window, text = "Identifiant :")
        self.uid = Entry (self.create_account_window, width = 30)
        label_Id.grid(row=1,column=1)
        self.uid.grid(row=1,column=2)

        # Pwd1 field
        label_pwd1 = Label (self.create_account_window, text = "Mot de passe :")
        self.pwd1 = Entry (self.create_account_window, width = 30, show='*')
        label_pwd1.grid(row=2,column=1)
        self.pwd1.grid(row=2,column=2)

        # Pwd2 field
        label_pwd2 = Label (self.create_account_window, text = "Répétez mot de passe :")
        self.pwd2 = Entry (self.create_account_window, width = 30, show='*')
        label_pwd2.grid(row=3,column=1)
        self.pwd2.grid(row=3,column=2)

        sdl = Label (self.create_account_window, text = "")
        sdl.grid(row=4,column=2)

        # button 'Valider'
        btnCpt = Button(self.create_account_window, text="Valider", command = self.validate_account_creation)
        btnCpt.grid(row=4,column=2)

        #close window
        btnQuit = Button(self.create_account_window, text = "Quitter", command = self.quit)
        btnQuit.grid(row=4,column=3)

        self.create_account_window.mainloop()






####################################################################
####    STUDENT FORM                                            ####
####################################################################
    def display_student_form(self):


        fiche = Tk()
        canvas_width = 80
        canvas_height = 80
        fiche.title('Fiche étudiant')

        numero = "987652478"
        statut = "normal"

        sais_photo = ""
        sais_nom = ""
        sais_prenom = ""
        sais_adresse_num = ""
        sais_adresse_voie = ""
        sais_adresse_cp = ""
        sais_adresse_ville = ""
        sais_telephone = ""
        sais_courriel = ""

        label_num = Label (fiche, text="Numéro : ")
        num = Label (fiche, text=numero)
        label_photo = Label (fiche, text="Photo : ")
        photo =  Entry (fiche, width=30, state=statut, textvariable=sais_photo)
        btn_photo = Button(fiche, text="Charger une photo", state=statut, command = self.sans_objet)
        canvas = Canvas(fiche, bg = 'white', width = canvas_width, height = canvas_height)
        label_nom = Label (fiche, text="Nom : ")
        nom = Entry (fiche, width=30, state=statut, textvariable=sais_nom)
        label_prenom = Label (fiche, text="Prénom : ")
        prenom = Entry (fiche, width=30, state=statut, textvariable=sais_prenom)
        label_adresse = Label (fiche, text="ADRESSE")
        label_adresse_num = Label (fiche, text="Numéro : ")
        adresse_num =  Entry (fiche, width=30, state=statut, textvariable=sais_adresse_num)
        label_adresse_voie = Label (fiche, text="Voie : ")
        adresse_voie =  Entry (fiche, width=30, state=statut, textvariable=sais_adresse_voie)
        label_adresse_cp = Label (fiche, text="Code postal : ")
        adresse_cp =  Entry (fiche, width=30, state=statut, textvariable=sais_adresse_cp)
        label_adresse_ville = Label (fiche, text="Ville : ")
        adresse_ville =  Entry (fiche, width=30, state=statut, textvariable=sais_adresse_ville)
        label_telephone = Label (fiche, text="Téléphone : ")
        telephone =  Entry (fiche, width=30, state=statut, textvariable=sais_telephone)
        label_courriel = Label (fiche, text="Courriel : ")
        courriel =  Entry (fiche, width=30, state=statut, textvariable=sais_courriel)
        sdl = Label (fiche, text = "")
        btn_enregistrer = Button(fiche, text="Enregistrer", state=statut, command = self.sans_objet)
        btn_supprimer = Button(fiche, text="Supprimer", state=statut, command = self.sans_objet)
        btnQuit = Button(fiche, text = "Quitter", command = fiche.quit)

        label_num.grid(row=1,column=1)
        num.grid(row=1,column=2)
        label_photo.grid(row=2,column=1)
        photo.grid(row=2,column=2)
        btn_photo.grid(row=2,column=3)
        canvas.grid(row=2,column=4)
        label_nom.grid(row=3,column=1)
        nom.grid(row=3,column=2)
        label_prenom.grid(row=4,column=1)
        prenom.grid(row=4,column=2)
        label_adresse.grid(row=5,column=2)
        label_adresse_num.grid(row=6,column=1)
        adresse_num.grid(row=6,column=2)
        label_adresse_voie.grid(row=6,column=3)
        adresse_voie.grid(row=6,column=4)
        label_adresse_cp.grid(row=7,column=1)
        adresse_cp.grid(row=7,column=2)
        label_adresse_ville.grid(row=7,column=3)
        adresse_ville.grid(row=7,column=4)
        label_telephone.grid(row=8,column=1)
        telephone.grid(row=8,column=2)
        label_courriel.grid(row=9,column=1)
        courriel.grid(row=9,column=2)
        sdl.grid(row=10,column=2)
        btn_enregistrer.grid(row=11,column=1)
        btn_supprimer.grid(row=11,column=3)
        btnQuit.grid(row=11,column=5)

        fiche.mainloop()

###############################################################

    def click_on_display_student_list(self):
        self.shuttle = ["students_list"]
        self.Men_window.destroy()

###############################################################
####    STUDENT LIST                                       ####
###############################################################
    def display_student_list(self):

        StudiantList = Tk()
        StudiantList.title('Liste des étudiants')

        student_num= "numéro étudiant"
        student_lastname= "nom etudiant"
        student_firstname="prenom etudiant"
        statut="active"

        for line in range(5):
            line_student = Label(StudiantList, text='   %s | %s | %s   ' % (student_num, student_lastname, student_firstname))
            btn_visu = Button(StudiantList, text="Afficher", state=statut, command = self.display_student_form)
            btn_del = Button(StudiantList, text="Supprimer", state=statut, command = self.sans_objet)
            line_student.grid(row=line, column=2)
            btn_visu.grid(row=line, column=3)
            btn_del.grid(row=line, column=4)


        btnQuit = Button(StudiantList, text = "Quitter", command = StudiantList.quit)
        btnQuit.grid(row=6,column=5)


        StudiantList.mainloop()

###############################################################



###############################################################
####    USER MENU                                          ####
###############################################################
    def display_user_menu(self):

        self.Men_window = Tk()

        self.Men_window.title('Menu')

        btnCreate = Button(self.Men_window, text = "Création de fiche", command = self. display_student_form)
        btnCreate.grid(row=4,column=1) 


        btnVisu = Button(self.Men_window, text="Afficher la liste des étudiants", command = self.click_on_display_student_list)
        btnVisu.grid(row=4,column=2)

        #fin du traitement et fermetre de la fenêtre
        btnQuit = Button(self.Men_window, text = "Quitter", command = self.Men_window.quit)
        btnQuit.grid(row=4,column=3)  

        self.Men_window.mainloop()
