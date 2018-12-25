### Exemple du code couleur des résistances électriques ###


from math import log10
from tkinter import Button, Canvas, Entry, Label, Tk


class Application:
    """Cette classe encapsule toute l'application.
    """

    def __init__(self):
        """Le constructeur de la classe : cette méthode spéciale / magique permet de créer et initialiser une instance de cette classe.
        """
        # création de la fenêtre de l'application, appelée 'root' ici
        self.root = Tk()
        self.root.title("Code des couleurs")

        # dessin initial de la résistance
        # la fonction qui suit "externalise" une partie de l'initialisation ce qui n'est pas une bonne pratique
        self.draw_resistor()

        # création d'une étiquette et de deux boutons
        Label(
            self.root, text="Entrez la valeur de la résisitance, en ohms :"
        ).grid(row=2, column=1, columnspan=3)

        Button(
            self.root, text="Montrer", command=self.change_colors
        ).grid(row=3, column=1)

        Button(
            self.root, text="Quitter", command=self.root.quit
        ).grid(row=3, column=3)

        # création de la zone de saisie pour l'utilisateur
        self.input_zone = Entry(self.root, width=28)
        self.input_zone.grid(row=3, column=2)

        # ce tableau donne le code couleur en associant chaque couleur à son index
        self.color_code = [
            'black', 'brown', 'red', 'orange', 'yellow',
            'green', 'blue', 'purple', 'grey', 'white'
        ]

        # l'initialisation de l'instance s'achève en lançant le réceptionnaire d'événements mais il vaudrait mieux le faire en dehors du constructeur
        self.root.mainloop()

    def draw_resistor(self):
        """Créé un canevas (zone de dessin) avec un modèle de résistance à trois bandes colorées.
        Attention !!! Cette méthode ajoute les attributs 'canvas' et 'strips' en dehors du constructeur __init__. C'est une pratique à éviter : le code gagne en lisibilité immédiate mais, dans un projet ambitieux, il sera compliqué de retrouver où ces attributs ont été définis.
        """
        # création de la zone de dessin : 'canvas' est une instance de la classe 'Canvas' de tkinter
        self.canvas = Canvas(self.root, width=500, height=200, bg='ivory')
        self.canvas.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # dessin de la résistance : un rectangle sur une ligne horizontale
        self.canvas.create_line(20, 100, 480, 100, width=5)
        self.canvas.create_rectangle(
            130, 60, 370, 140, fill='light grey', width=3
        )

        # dessin des trois bandes (noires au départ)
        self.strips = []  # cette liste contiendra les 3 bandes
        for x in range(170, 300, 48):
            self.strips.append(
                self.canvas.create_rectangle(
                    x, 62, x + 24, 139, fill='black', width=0
                )
            )

    def change_colors(self):
        """Analyse l'entrée de l'utilisateur pour déterminer les couleurs des trois bandes.
        Là encore, la méthode créé un nouvel attribut 'user_input' ce qui n'est pas une bonne pratique.
        """
        # récupération de la saisie de l'utilisateur
        self.user_input = self.input_zone.get()

        # conversion de l'entrée avec un gestionnaire d'exception try-except-else
        try:
            value = int(self.user_input)
        except:
            error_code = 1  # code d'erreur si la conversion lève une exception
        else:
            error_code = 0

        # si l'entrée ne convient pas, on appelle la méthode 'raise_error'
        if error_code == 1 or value < 10 or value > 1e11:
            self.raise_error()

        # sinon on traite la valeur entrée par l'utilisateur
        else:
            codes = [0, 0, 0]  # liste recueillant les 3 codes couleurs

            # on récupère le nombre de chiffres avec le logarithme décimal
            max_exponent = int(log10(value))

            # on obtient alors un ordre de grandeur de 'value' sous la forme d'une puissance de 10
            magnitude_order = 10 ** max_exponent

            # on récupère alors le chiffre le plus à gauche...
            codes[0] = int(value / magnitude_order)

            # ... puis celui à côté...
            decimal_part = value / magnitude_order - codes[0]
            codes[1] = int(decimal_part * 10 + 0.5)

            # ... et enfin le nombre de zéros après les deux premiers chiffres
            codes[2] = max_exponent - 1

            # on met alors à jour les trois bandes de couleurs
            for n in range(3):
                self.canvas.itemconfigure(
                    self.strips[n], fill=self.color_code[codes[n]]
                )

    def raise_error(self):
        """Colore la zone d'entrée en rouge pendant une seconde.
        La remise à zéro de la zone de saisie est gérée par la méthode 'clear_input_zone'.
        """
        self.input_zone.configure(bg='red')
        self.root.after(1000, self.clear_input_zone)

    def clear_input_zone(self):
        """Recolore la zone d'entrée en blanc et supprime la saisie de l'utilisateur.
        """
        self.input_zone.configure(bg='white')
        self.input_zone.delete(0, len(self.user_input))


"""Le script principal qui suit ne s'exécute que si ce fichier est appelé directement (il ne s'exécutera pas si le fichier est importé par un autre script).
"""
if __name__ == '__main__':
    app = Application()
