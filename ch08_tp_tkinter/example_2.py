### Exemple de la cible et du visage ###


from tkinter import Button, Canvas, Tk, ALL, LEFT, RIGHT, TOP


def draw_circle(x0, y0, radius, color='black'):
    """Trace le cercle de centre (x0, y0) et de rayon 'radius'.
    La couleur du tracé est donné par 'color' (couleur 'black' par défaut).
    """
    canvas.create_oval(
        x0 - radius, y0 - radius, x0 + radius, y0 + radius, outline=color
    )


def draw_figure_1():
    """Dessine une cible avec un viseur.
    """
    # On efface d'abord le canevas (la zone de dessin)
    canvas.delete(ALL)
    # On trace les deux axes du viseur
    canvas.create_line(200, 0, 200, 400, fill='blue')
    canvas.create_line(0, 200, 400, 200, fill='blue')
    # On trace les cercles concentriques de la cible
    radius = 30
    while radius < 200:
        draw_circle(200, 200, radius)
        # le 4ème paramètre, 'color', n'étant pas renseigné, il prendra sa valeur par défaut : les cercles seront donc tous tracés en noir
        radius += 30


def draw_figure_2():
    """Dessine un visage schématique.
    """
    canvas.delete(ALL)
    # On stocke les paramètres de chaque cercle dans une liste de listes, chacune stockant les coordonnées du centre, le rayon et la couleur du tracé
    circles = [
        [200, 200, 160, 'red'],
        [140, 140, 30, 'blue'],
        [260, 140, 30, 'blue'],
        [140, 140, 10, 'black'],
        [260, 140, 10, 'black'],
        [88, 230, 40, 'red'],
        [312, 230, 40, 'red'],
        [200, 190, 30, 'purple'],
        [200, 290, 60, 'purple']
    ]
    # On trace les cercles en parcourant la liste 'circles'
    for circle in circles:
        # On 'unpack' les 4 éléments de la liste 'circle'...
        x0, y0, radius, color = circle
        # ... pour obtenir un code plus lisible (et moins de [] aussi...)
        draw_circle(x0, y0, radius, color)


##### Programme principal #####

window = Tk()
canvas = Canvas(window, width=400, height=400, bg='ivory')
canvas.pack(side=TOP, padx=5, pady=5)
btn1 = Button(window, text="dessin 1", command=draw_figure_1)
btn1.pack(side=LEFT, padx=3, pady=3)
btn2 = Button(window, text="dessin 2", command=draw_figure_2)
btn2.pack(side=RIGHT, padx=3, pady=3)

window.mainloop()
