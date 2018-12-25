### Exemple du petit train ###


from tkinter import Button, Canvas, Tk, LEFT, TOP


def draw_circle(canvas, x0, y0, r):
    """Dessine un cercle de centre (x0, y0) et de rayon 'r' dans la zone de dessin 'canvas'.
    """
    canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r)


class Application(Tk):
    """La classe 'Application' hérite de la classe 'Tk' et en récupère tous les attributs et toutes les méthodes.
    """

    def __init__(self):
        """Le constructeur de l'application instancie la fenêtre, le canevas (la zonde de dessin) et deux boutons.
        """
        # initialisation de la fenêtre
        Tk.__init__(self)
        # initialisation de la zone de dessin
        self.canvas = Canvas(self, width=950, height=260, bg='white')
        self.canvas.pack(side=TOP, padx=5, pady=5)
        # ajout des bottons 'Train' et 'Hello
        Button(self, text="Train", command=self.draw_train).pack(side=LEFT)
        Button(self, text="Hello", command=self.hello).pack(side=LEFT)

    def draw_train(self):
        """Dessine les 4 wagons dans le canevas.
        """
        self.wagon1 = Wagon(self.canvas, 20, 60)
        self.wagon2 = Wagon(self.canvas, 260, 60)
        self.wagon3 = Wagon(self.canvas, 500, 60)
        self.wagon4 = Wagon(self.canvas, 740, 60)

    def hello(self):
        """Dessine 4 passagers aux fenêtres du train.
        """
        self.wagon1.passenger(3)  # à la 3ème fenêtre du 1er wagon
        self.wagon3.passenger(1)  # à la 1ère fenêtre du 3ème wagon
        self.wagon3.passenger(2)  # à la 2ème fenêtre du 3ème wagon
        self.wagon4.passenger(1)  # à la 1ère fenêtre du 4ème wagon


class Wagon:
    def __init__(self, canvas, x, y):
        """Dessine un wagon sur le canevas 'canvas', son coin supérieur gauche se trouvant aux coordonnées (x, y).
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        # cadre du wagon
        self.canvas.create_rectangle(x, y, x + 190, y + 120)
        # fenêtres du wagon écartées de 60 pixels
        for window_x in range(x + 10, x + 180, 60):
            canvas.create_rectangle(window_x, y + 10, window_x + 50, y + 80)
        # roues du wagon de rayon 24 pixels
        draw_circle(self.canvas, x + 36, y + 146, 24)
        draw_circle(self.canvas, x + 144, y + 146, 24)

    def passenger(self, window):
        """Dessine un passager à la fenêtre numéro 'window' du wagon instancié.
        """
        passenger_x = self.x + window * 60 - 24
        passenger_y = self.y + 50
        # visage du passager
        draw_circle(self.canvas, passenger_x, passenger_y, 20)
        # oeil gauche
        draw_circle(self.canvas, passenger_x - 10, passenger_y, 4)
        # oeil droit
        draw_circle(self.canvas, passenger_x + 10, passenger_y, 4)
        # bouche
        draw_circle(self.canvas, passenger_x, passenger_y + 10, 3)


if __name__ == '__main__':
    app = Application()
    app.mainloop()
