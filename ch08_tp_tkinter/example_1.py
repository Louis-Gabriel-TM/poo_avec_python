### Exemple des faisceaux de droites colorées ###


from tkinter import Button, Canvas, Tk, LEFT, BOTTOM
from random import choice


def draw_line():
    """Trace la ligne dans le canevas 'canvas' joignant
    les points (x1, y1) et (x2, y2) et de couleur 'color'.
    """
    global y1, y2
    canvas.create_line(x1, y1, x2, y2, width=2, fill=color)
    y1 -= 10
    y2 += 10


def change_color():
    """Change la couleur des tracés en la choisissant au hasard
    dans une liste prédéfinie.
    """
    global color
    color_palette = [
        'purple', 'cyan', 'brown', 'green', 'red', 'blue', 'orange', 'yellow'
    ]
    color = choice(color_palette)


"""Fonction constituant le coeur du script.
"""
# Initialisation des extrémités et de la couleur du tracé
x1, y1 = 10, 390
x2, y2 = 390, 10
color = 'dark green'
# Création de la fenêtre
window = Tk()
# Création de la zone de dessin
canvas = Canvas(window, bg='dark grey', height=400, width=400)
canvas.pack(side=LEFT)  # Accrochage sur la fenêtre
# Création du boutton 'Quitter'
btn1 = Button(window, text="Quitter", command=window.quit)
btn1.pack(side=BOTTOM)  # Accrochage sur la fenêtre
# Création des boutons 'Tracer une ligne' et 'Autre couleur'
btn2 = Button(window, text="Tracer une ligne", command=draw_line)
btn2.pack()  # Accrochage sur la fenêtre (en haut par défaut)
btn3 = Button(window, text="Autre couleur", command=change_color)
btn3.pack()
# Lancement du réceptionnaire d'événements de la fenêtre
window.mainloop()
# Destruction / fermeture de la fenêtre
window.destroy()
