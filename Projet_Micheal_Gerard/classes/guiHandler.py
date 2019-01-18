
from tkinter import Button, Canvas, Tk, ALL, LEFT, RIGHT, TOP, Label, BOTTOM, Entry

class Gui_handler:

    def __init__(self,shuttle1):
        self.shuttle1= shuttle1
        

    def display_login(self):
        try :
            self.window2.destroy()
        except :
            pass

        try :
            self.window3.destroy()
        except :
            pass

        self.window1 = Tk()
        self.window1.title("page d'acceuil")
        self.label1 = Label(self.window1, text='Entrer votre mot de passe', fg='grey')
        self.label1.pack(side=LEFT, padx=3, pady=3)
        self.E1 = Entry(self.window1, bd =2)
        self.E1.pack(side = LEFT)
        self.btn1 = Button(self.window1, text="ENTRER", command=self.login_choice)
        self.btn1.pack(side=BOTTOM, padx=3, pady=3)
        self.window1.mainloop()

    def login_choice(self):
        """ loginchoice
        """
        if self.E1.get() == "admin":
            self.display_admin()
        elif self.E1.get() == "":
            self.display_student()
        else:
            self.window1.destroy()
            self.display_login()

    def display_admin(self):
        pass

    def display_student(self):
        self.window1.destroy()
        self.window2 = Tk()
        self.window2.title("page d'acceuil ETUDIANT")
        self.label2 = Label(self.window2, text='Vous ètes connecté en tant qu\'étudiant, que souhaitez vous faire?', fg='grey')
        self.label2.pack(side=TOP, padx=3, pady=3)

        self.btn2 = Button(self.window2, text="CONSULTER fiche", command=self.display_choice_profile)
        self.btn2.pack(side=LEFT, padx=3, pady=3)
      
        self.btn3= Button(self.window2, text="CREER fiche", command=self.display_form)
        self.btn3.pack(side=LEFT, padx=3, pady=3)
        
        self.btn4= Button(self.window2, text="SORTIR", command=self.display_login)
        self.btn4.pack(side=RIGHT, padx=3, pady=3)

        self.window2.mainloop()

    def display_choice_profile(self):
        try :
            self.window2.destroy()
        except :
            pass
        
        self.window3 = Tk()
        self.window3.title("Liste des étudiants")
        self.label2 = Label(self.window3, text='Appuyez sur le bouton a droite du nom prenom de l\'etudiant pour consulter sa fiche', fg='grey')
        self.label2.pack(side=TOP, padx=3, pady=3)

        liste = self.get_shuttle1()
        first_name,last_name = liste[0][0:2]


        self.label3 = Label(self.window3, text=first_name +" "+ last_name, fg='grey')
        self.label3.pack(side=LEFT, padx=3, pady=3)

        self.btn5 = Button(self.window3, text="OK", command=self.display_select_menu)
        self.btn5.pack(side=RIGHT, padx=3, pady=3)

        self.btn6 = Button(self.window3, text="SORTIR", command=self.display_login)
        self.btn6.pack(side=BOTTOM, padx=3, pady=3)
        self.window3.mainloop()


    def display_select_menu(self):
        try :
            self.window3.destroy()
        except :
            pass


        self.window4 = Tk()
        self.window4.title("informations personnelles :")


        self.label4 = Label(self.window4, text=self.get_shuttle1(), fg='grey')
        self.label4.pack(side=TOP, padx=3, pady=3)
        

    def display_form(self):
       pass

    def display_valid_creation(self):
        pass

    def display_admin(self):
        pass
    
    def display_valid_suppression(self):
        pass

    def get_shuttle1(self):
        return self.shuttle1

    

if __name__ == "__main__":
    newWindow = Gui_handler()
    newWindow.display_login()
