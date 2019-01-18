from tkinter import Tk, Label, Button, Canvas, LEFT, BOTTOM, TOP, RIGHT, Entry, DISABLED

class myGUIhandler:
    def __init__(self, db):
        ''' self.entree vaut un widget Entry
            self.chaine vaut un widget Label
        '''
        self.mot_de_passe = ''
        self.entree = None  # Entry pour mot_de_passe
        self.chaine = None  # Label
        self.fen1 = None # Fenetre

        self.entree1 = None # name
        self.entree2 = None # lastname
        self.entree3 = None # number
        self.entree4 = None # street
        self.entree5 = None # zipcode
        self.entree6 = None # city
        # on ne gère pas les images

        self.db = db
        pass

    def evaluer2(self):
        self.evaluer('')

    def evaluer(self, event):
        #print(chaine.keys())
        if self.entree.get() == "" or self.entree.get() == "admin":
            # if self.entree.get() == "admin":
            #     self.chaine.configure(text = "Admin", fg="green")
            # else:
            #     self.chaine.configure(text = "Etudiant", fg="green")
            if self.entree.get() == "": 
                self.mot_de_passe = 'etudiant'
            else:
                self.mot_de_passe = self.entree.get()
            self.fen1.quit()
        else:
            self.chaine.configure(text = "Mot de passe non valide", fg="red")
        self.chaine.pack()
        pass

    def display_login(self):
        # Création du widget principal ("maître") :
        self.fen1 = Tk()
        self.fen1.title('Bienvenue sur ce site "Alumni"')
        
        bou1 = Button(self.fen1,text='OK',command=self.evaluer2)
        bou1.pack(side=BOTTOM)
     
        labelPseudo = Label(self.fen1, text="Mot de passe")
        labelPseudo.pack(side=LEFT)
        self.entree = Entry(self.fen1, show="*")
        self.entree.bind("<Return>", self.evaluer)
        self.chaine = Label(self.fen1)
        self.entree.pack(side=LEFT)
        self.chaine.pack()

        self.fen1.mainloop() # démarrage du réceptionnaire d’événements
        self.fen1.destroy()  # destruction (fermeture) de la fenêtre

        return self.mot_de_passe

    def creer(self):
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

        bou1 = Button(self.fen2,text='CREER',command=self.creation)
        bou1.grid(row=7, column=0)
        pass
    def creation(self):
        self.db.CREATE([self.entree1.get(), self.entree2.get(), self.entree3.get(), self.entree4.get(), self.entree5.get(), self.entree6.get()])
        pass
    def consulter(self):
        self.db.READ()
        pass
    def modifier(self):
        if ( self.entree1 == None ):
            pass
        else:
            self.db.UPDATE([self.entree1.get(), self.entree2.get(), self.entree3.get(), self.entree4.get(), self.entree5.get(), self.entree6.get()])
        pass
    def supprimer(self):
        if ( self.entree1 == None ):
            pass
        else:
            self.db.DELETE([self.entree1.get()])
        pass
    def display_form(self):
        self.fen2 = Tk()
        self.fen2.title('Bienvenue sur ce site "Alumni"')

        bou1 = Button(self.fen2,text='CREATION',command=self.creer)
        bou1.grid(row=0, column=0)
        bou1 = Button(self.fen2,text='CONSULTER',command=self.consulter)
        bou1.grid(row=0, column=1)

        if self.mot_de_passe == 'admin':
            bou1 = Button(self.fen2,text='MODIFIER',command=self.modifier)
            bou2 = Button(self.fen2,text='SUPPRIMER',command=self.supprimer)
        else:
            bou1 = Button(self.fen2,text='MODIFIER',command=self.modifier,state=DISABLED)
            bou2 = Button(self.fen2,text='SUPPRIMER',command=self.supprimer,state=DISABLED)
            
        bou1.grid(row=0, column=2)
        bou2.grid(row=0, column=3)
     
        self.fen1.mainloop() # démarrage du réceptionnaire d’événements
        #fen1.destroy()  # destruction (fermeture) de la fenêtre
        pass
    pass

if __name__ == '__main__':

    gui = myGUIhandler(None)
    mdp = gui.display_login()
    print (mdp)
    gui.display_form()