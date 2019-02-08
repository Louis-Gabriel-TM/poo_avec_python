from tkinter import Tk, Label, Button, Canvas, LEFT, BOTTOM, TOP, RIGHT, Entry, DISABLED, messagebox, Scrollbar, Listbox, VERTICAL, END, Y, BOTH
import hashlib


class myGUIhandler:
    def verification_des_entrees(self):
        ''' vérifie que les entrées numériques sont bien des nombres '''
        ok = 0
        if not ( str(self.entree3.get()).isdigit() ) : ok = 3
        if not ( str(self.entree5.get()).isdigit() ) : ok = 5
        if not ( str(self.entree7.get()).isdigit() ) : ok = 7
        if not ( self.entree8.get().find('@') != -1 and self.entree8.get().find('@') != 0 and self.entree8.get().find('@') != len(self.entree8.get())-1 and
                ( self.entree8.get().split('@')[1].split('.')[1] == 'fr' or self.entree8.get().split('@')[1].split('.')[1] == 'com' )
            ): ok = 8
        return ok

    def __init__(self, db):
        ''' self.entree vaut un widget Entry
            self.chaine vaut un widget Label
        '''
        self.mot_de_passe = ''
        self.user = ''

        self.ident = None   # Entry identifiant
        self.mdp = None     # Entry mdp
        self.chaine = None  # Label
        self.fen1 = None  # Fenetre

        self.entree1 = None # name
        self.entree2 = None # lastname
        self.entree3 = None # number
        self.entree4 = None # street
        self.entree5 = None # zipcode
        self.entree6 = None # city
        self.entree7 = None # phone number
        self.entree8 = None # email
        self.entree9 = None # link_photo
        # on ne gère pas les images

        self.mdps = None    # table des mots de passe

        self.db = db
        pass

    def verif_mdp(self, s):
        ''' vérification que le mot de passe à plus de 8 lettres(sauf admin) une minuscule, une majuscule '''
        ok = False
        isnum = False
        isMaj = False
        isMin = False
        for x in s:
            if str.isdigit(x):
                isnum = True
            if str.isupper(x):
                isMaj = True
            if str.islower(x):
                isMin = True
        if isnum and isMaj and isMin:
            ok = True
        if len(self.mdp.get()) >= 8 and ok:
            pass
        else:
            messagebox.showerror("Mot de passe non conforme", "8 chiffres avec une majuscule, une minuscule et un chiffre minimum")

    def evaluer3(self):
        ''' méthode pour créer un compte
        '''
        if self.db == None:
            pass
        else:
            self.db.ecris_db_mdp(self.ident.get(), hashlib.md5(self.mdp.get().encode('UTF-8')).hexdigest())
            self.mdps = self.db.readmdp()
     
    def evaluer2(self):
        ''' méthode pour vérifier la saisie lors du login
        '''
        self.evaluer('')

    def evaluer(self, event):
        ''' méthode pour vérifier la saisie lors du login
        '''
        if self.ident.get() == "admin":
            self.chaine.configure(text = "Admin", fg="brown")
        else:
            self.chaine.configure(text = "Etudiant", fg="green")

        if self.mdp.get() == "" or self.ident.get() == "":
            self.chaine.configure(text = "Mdp ou identifiant vide", fg="red")
        else:
            # vérification du mot de passe uniquement pour etudiant
            if self.ident.get() != 'admin':
                self.verif_mdp(self.mdp.get())

            #print ( mdps )
            for x in self.mdps:
                user, mdp = x                                           #'\uFEFF'.encode('UTF-8')
                if user == self.ident.get() and mdp == hashlib.md5(self.mdp.get().encode('UTF-8')).hexdigest():
                    print ( "Utilisateur ", user, "mot de passe ", mdp)
                    self.mot_de_passe = self.ident.get()
                    self.user = self.ident.get()
                    if self.ident.get() != 'admin':
                        self.mot_de_passe = 'etudiant'
                    break
            if self.mot_de_passe == self.ident.get():
                pass
            else:
                self.chaine.configure(text = "Mot de passe non valide", fg="red") 
        self.chaine.grid(row=2, column=1)

        if self.mot_de_passe == 'admin' or self.mot_de_passe == 'etudiant':
            self.fen1.quit()
        pass

    def display_login(self):
        ''' création de la fenêtre de login
        '''
        # Création du widget principal ("maître") :
        self.fen1 = Tk()

        w = 220 # width for the Tk root
        h = 100 # height for the Tk root

        # get screen width and height
        ws = self.fen1.winfo_screenwidth() # width of the screen
        hs = self.fen1.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        self.fen1.geometry('%dx%d+%d+%d' % (w, h, x, y))

        if self.db == None:
            pass
        else:
            self.mdps = self.db.readmdp()

        self.fen1.title('Bienvenue sur ce site "Alumni"')

        bou1 = Button(self.fen1,text='CONNEXION',command=self.evaluer2)
        bou1.grid(row=3, column=0)

        bou2 = Button(self.fen1,text='CREER COMPTE',command=self.evaluer3)
        bou2.grid(row=3, column=1)

        labelPseudo = Label(self.fen1, text="    Identifiant", justify='right')
        labelPseudo.grid(row=0, column=0)
        self.ident = Entry(self.fen1)
        self.ident.bind("<Return>", self.evaluer)
        self.ident.grid(row=0, column=1)
        self.chaine = Label(self.fen1)
        self.chaine.grid(row=2, column=1)

        labelMdp = Label(self.fen1, text="Mot de passe", justify='right')
        labelMdp.grid(row=1, column=0)
        self.mdp = Entry(self.fen1, show="*")
        self.mdp.bind("<Return>", self.evaluer)
        self.mdp.grid(row=1, column=1)
        self.chaine = Label(self.fen1)
        self.chaine.grid(row=2, column=1)

        self.fen1.mainloop() # démarrage du réceptionnaire d’événements
        self.fen1.destroy()  # destruction (fermeture) de la fenêtre

        return self.mot_de_passe

    def creer(self):
        ''' affiche le volet du formulaire de la fiche '''

        entree1 = Label(self.fen2, text="        Name", justify='right')
        entree1.grid(row=1, column=0)
        self.entree1 = Entry(self.fen2)
        self.entree1.grid(row=1, column=1)

        entree2 = Label(self.fen2, text="   Lastname", justify='right')
        entree2.grid(row=2, column=0)
        self.entree2 = Entry(self.fen2)
        self.entree2.grid(row=2, column=1)

        entree3 = Label(self.fen2, text="     Numero", justify='right')
        entree3.grid(row=3, column=0)
        self.entree3 = Entry(self.fen2)
        self.entree3.grid(row=3, column=1)

        entree4 = Label(self.fen2, text="Street name ", justify='right')
        entree4.grid(row=4, column=0)
        self.entree4 = Entry(self.fen2)
        self.entree4.grid(row=4, column=1)

        entree5 = Label(self.fen2, text="    ZIP code", justify='right')
        entree5.grid(row=5, column=0)
        self.entree5 = Entry(self.fen2)
        self.entree5.grid(row=5, column=1)

        entree6 = Label(self.fen2, text="            City", justify='right')
        entree6.grid(row=6, column=0)
        self.entree6 = Entry(self.fen2)
        self.entree6.grid(row=6, column=1)

        entree7 = Label(self.fen2, text="    phone number", justify='right')
        entree7.grid(row=7, column=0)
        self.entree7 = Entry(self.fen2)
        self.entree7.grid(row=7, column=1)

        entree8 = Label(self.fen2, text="           email", justify='right')
        entree8.grid(row=8, column=0)
        self.entree8 = Entry(self.fen2)
        self.entree8.grid(row=8, column=1)

        entree9 = Label(self.fen2, text="            photo", justify='right')
        entree9.grid(row=9, column=0)
        self.entree9 = Entry(self.fen2)
        self.entree9.grid(row=9, column=1)

        bou1 = Button(self.fen2,text='CREER UNE FICHE',command=self.creation)
        bou1.grid(row=10, column=1)
        pass

    def creation(self):
        ''' créer la partie création de l'interface
        '''
        if self.mot_de_passe == 'admin' or self.mot_de_passe == 'etudiant' and ( self.user.upper() == self.entree1.get().upper() ):
            if self.verification_des_entrees() == 0:
                # Recherche d'un fiche existante
                l = self.db.read(1)
                trouve = False
                for e in l:
                    if ( e[0] == self.entree1.get() ):
                        trouve = True
                if not trouve:
                    self.db.create([self.entree1.get(), self.entree2.get(), self.entree3.get(), self.entree4.get(), self.entree5.get(), self.entree6.get(), self.entree7.get(), self.entree8.get(), self.entree9.get()])
                    if self.mot_de_passe == 'admin':
                        self.db.ecris_db_mdp(self.entree1.get(), hashlib.md5( (self.entree1.get().lower().capitalize() + self.entree1.get().lower() + "42").encode('UTF-8')).hexdigest())
                else:
                    messagebox.showwarning("Création de fiche", "Fiche " + self.entree1.get() + " existe déjà !")

            else:
                messagebox.showinfo("Vérification du format des entrées", "Champ n°" + str(self.verification_des_entrees()) + " en erreur")
                pass
            pass
        else:
            messagebox.showinfo("Droit d'accès", "Pour créer la fiche " + self.entree1.get().upper() + ", il faut être admin ou vous pouvez uniquement créer votre fiche " + self.user.upper())

    def consulter(self):
        ''' affiche sur la console et dans une listebox, les lignes tronquées de la table Students '''
        lignes = self.db.read(1)

        self.fen3 = Tk()
        self.fen3.title('Visualisation des données alumni')

        scrollbar = Scrollbar(self.fen3)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.listbox = Listbox(self.fen3, yscrollcommand=scrollbar.set, width=-1)
        self.listbox.bind("<ButtonRelease-1>",self.cliqueLigne)
        for i,l in enumerate( lignes ):
            print ( i, l )
            la = l[0][:15]
            la = la.ljust(15, ' ')
            la = la + l[1][:15]
            la = la.ljust(30, ' ')
            la = la + l[5][:15]
            la = la.ljust(45, ' ')
            self.listbox.insert(END, la)

        self.listbox.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=self.listbox.yview)
        self.fen3.mainloop()
        #self.fen3.destroy()

    def modifier(self):
        ''' Update à partir du nom de la fiche courante '''
        if ( self.entree1 == None or self.entree1.get() == '' ):
           pass
        else:
            if self.mot_de_passe == 'admin' or self.mot_de_passe == 'etudiant' and ( self.user.upper() == self.entree1.get().upper() ):
                self.db.update([self.entree1.get(), self.entree2.get(), self.entree3.get(), self.entree4.get(), self.entree5.get(), self.entree6.get(), self.entree7.get(), self.entree8.get(), self.entree9.get()])
            else:
                messagebox.showinfo("Droit d'accès", "Pour modifier la fiche " + self.entree1.get().upper() + ", il faut être admin ou vous pouvez modifier uniquement la fiche " + self.user.upper())
            pass
        pass

    def supprimer(self):
        ''' supprime à partir des champs nom, city et email soient requis '''
        if ( self.entree1 == None or self.entree6 == None or self.entree8 == None 
            or self.entree1.get() == '' or self.entree6.get() == '' or self.entree8.get() == '' ):
            messagebox.showinfo("Informations manquantes", "nom + city + email, doivent être renseignés pour supprimer." )
        else:
            print( self.mot_de_passe )
            print ( self.user )
            print ( self.entree1.get() )
            print ( self.entree6.get() )
            print ( self.entree8.get() )
            if self.mot_de_passe == 'admin' or self.mot_de_passe == 'etudiant' and ( self.user.upper() == self.entree1.get().upper() ):
                self.db.deletes([self.entree1.get(), self.entree6.get(), self.entree8.get()])
            else:
                messagebox.showinfo("Droit d'accès", "Pour supprimer la fiche " + self.entree1.get().upper() + ", il faut être admin ou vous pouvez supprimer uniquement la fiche " + self.user.upper())
                pass
        pass

    def cliqueLigne(self, event):
        ''' selection du numéro de ligne pour la listebox '''
        try:
            nSel = self.listbox.curselection()[0]    # sélection
            self.entree1.delete(0, len(self.entree1.get()))
            self.entree1.insert(0, self.listbox.get(nSel).split(' ')[0])   # get() renvoie un tuple ou une liste ?
            self.trouver()
        except:
            pass
        pass

    def trouver(self):
        ''' affiche dans la fiche, les informations trouvées dans la base pour le nom de la fiche ''' 
        l = self.db.read(1)
        trouve = False
        for e in l:
            if ( self.entree1 != None and e[0] == self.entree1.get() ):
                trouve = True
                print ( "Trouvé ", e[0])
                #self.entree1.set(e[0])
                self.entree2.delete(0, len(self.entree2.get()))
                self.entree2.insert(0, e[1])
                self.entree3.delete(0, len(self.entree3.get()))
                self.entree3.insert(0, e[2])
                self.entree4.delete(0, len(self.entree4.get()))
                self.entree4.insert(0, e[3])
                self.entree5.delete(0, len(self.entree5.get()))
                self.entree5.insert(0, e[4])
                self.entree6.delete(0, len(self.entree6.get()))
                self.entree6.insert(0, e[5])
                self.entree7.delete(0, len(self.entree7.get()))
                self.entree7.insert(0, e[6])
                self.entree8.delete(0, len(self.entree8.get()))
                self.entree8.insert(0, e[7])
                self.entree9.delete(0, len(self.entree9.get()))
                self.entree9.insert(0, e[8])
        if not trouve:
            if self.entree1 != None:
                messagebox.showinfo("Recherche fiche", "Fiche de " + self.entree1.get() + " non trouvée !")

    def display_form(self):
        ''' affiche l'interface Alumni pour CRUD
        '''
        self.fen2 = Tk()

        if self.mot_de_passe == 'admin':
            self.fen2.title('Bienvenue sur ce site "Alumni" : droits ADMIN.')
        else:
            self.fen2.title('Bienvenue sur ce site "Alumni"')

        bou1 = Button(self.fen2,text='VOIR FICHE',command=self.creer)
        bou1.grid(row=0, column=0)
        bou1 = Button(self.fen2,text='CONSULTER',command=self.consulter)
        bou1.grid(row=0, column=1)
        
        #if self.mot_de_passe == 'admin':
        bou1 = Button(self.fen2,text='MODIFIER',command=self.modifier)
        bou2 = Button(self.fen2,text='SUPPRIMER',command=self.supprimer)
        bou3 = Button(self.fen2,text='TROUVER',command=self.trouver)
        #else:
        #    bou1 = Button(self.fen2,text='MODIFIER',command=self.modifier,state=DISABLED)
        #    bou2 = Button(self.fen2,text='SUPPRIMER',command=self.supprimer,state=DISABLED)
           
        bou1.grid(row=0, column=2)
        bou2.grid(row=0, column=3)
        bou3.grid(row=0, column=4)
     
        self.fen1.mainloop() # démarrage du réceptionnaire d’événements
        #fen1.destroy()  # destruction (fermeture) de la fenêtre
        pass
    pass

if __name__ == '__main__':
    import databaseHandler

    print ( 'ATTENTION : application lancée à partir de GUIhandler et non à partir du main.py' )

    db = databaseHandler.myDatabaseHandler()
    gui = myGUIhandler(db)
    mdp = gui.display_login()
    print (mdp)
    #gui.display_form()