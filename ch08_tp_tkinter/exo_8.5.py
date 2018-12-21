from tkinter import Button, Canvas, Tk, LEFT, BOTTOM
from random import choice


def draw_line():
    global y1, y2
    """
    Pour essayer les méthodes 'create_rectangle', 'create_arc', 'create_oval' et 'create_polygon', décommenter la ligne correspondante.
    """

    """Avec 'create_rectangle', (x1, y1) correspond au coin supérieur gauche du rectangle et (x2, y2) au coin inférieur droit.
    Les côtés du rectangle étant horizontaux et vertiacux.
    """
    #canvas.create_rectangle(x1, y1, x2, y2, width=2, fill=color)

    """
    Avec 'create_arc', on obtient un secteur de l'ellipse pleine inscrite dans le rectangle défini par (x1, y1) et (x2, y2).
    Par défaut, ce secteur couvre les angles de 0° à 90°...
    """
    #canvas.create_arc(x1, y1, x2, y2, width=2, fill=color)
    """
    ... ou les angles de 'start' à 'start' + 'extent' si on passe à la méthode des valeurs pour ces deux paramètres.
    """
    # canvas.create_arc(
    #    x1, y1, x2, y2, width=2, fill=color, start=45, extent=270)

    """
    Avec 'create_oval', on obtient une ellipse pleine inscrite dans le rectangle défini par (x1, y1) et (x2, y2).
    """
    #canvas.create_oval(x1, y1, x2, y2, width=2, fill=color)

    """
    Avec 'create_polygon', il nous faut passer au moins un troisième point en paramètre : on obtient alors le polygone plein reliant les points (x1, y1), (x2, y2), (x3, y3), ...
    """
    x3, y3 = 50, 50  # ajout d'un 3ème sommet...
    x4, y4 = 150, 150  # ... et d'un 4ème
    #canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, width=2, fill=color)
    """
    ... l'ordre des points jouant sur le polygone obtenu !
    """
    #canvas.create_polygon(x1, y1, x2, y2, x4, y4, x3, y3, width=2, fill=color)

    y1 -= 10
    y2 += 10


def change_color():
    global color
    color_palette = [
        'purple', 'cyan', 'brown', 'green', 'red', 'blue', 'orange', 'yellow'
    ]
    color = choice(color_palette)


x1, y1 = 10, 390
x2, y2 = 390, 10
color = 'dark green'

window = Tk()

canvas = Canvas(window, bg='dark grey', height=400, width=400)
canvas.pack(side=LEFT)

btn1 = Button(window, text="Quitter", command=window.quit)
btn1.pack(side=BOTTOM)

btn2 = Button(window, text="Tracer une ligne", command=draw_line)
btn2.pack()
btn3 = Button(window, text="Autre couleur", command=change_color)
btn3.pack()

window.mainloop()

window.destroy()
