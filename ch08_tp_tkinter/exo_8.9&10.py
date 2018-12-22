from random import choice
from tkinter import Button, Canvas, Tk, LEFT, RIGHT, TOP


def draw_square(x, y, color='white'):
    """Dessine un carré représentant une case du damier dont le coin supérieur gauche a pour coordonnées (x, y).
    Cette case est par défaut de couleur blanche.
    """
    canvas.create_rectangle(x, y, x + 39, y + 39, fill=color)


def draw_board():
    """Dessine le damier en utilisant une astuce pour déterminer la couleur de chaque case :
    1) on repère chaque colonne et chaque ligne par un nombre de 0 à 9,
    2) on remarque que si la somme de ces numéros est pair alors la case est noire et que si cette somme est impaire, la case est blanche.
    """
    for column in range(10):
        # range(10) génère tous les entiers de 0 à 10 exclus
        for line in range(10):
            # si le reste de la division par 2 est nul, la somme est paire
            if (column + line) % 2 == 0:
                draw_square(column * 40, line * 40, 'black')
            else:
                draw_square(column * 40, line * 40)


def draw_piece():
    """Dessine un disque rouge représentant un pion.
    Chaque coordonnée du centre étant tiré au hasard avec 'random.choice' dans la liste COORD_VALUES (cf. programme principal).
    """
    x0 = choice(COORD_VALUES)
    y0 = choice(COORD_VALUES)
    canvas.create_oval(x0 - 15, y0 - 15, x0 + 15, y0 + 15, fill='red')


##### Programme principal #####

window = Tk()
# Le damier comportant 10 * 10 cases, on a intérêt à prendre un multiple de 10 pour les dimensions du canevas (la zone de dessin)
canvas = Canvas(window, width=400, height=400, bg='ivory')

# On construit en fonction des dimensions du damier les valeurs que peuvent avoir les coordonnées des centres des pions
COORD_VALUES = [20, 60, 100, 140, 180, 220, 260, 300, 340, 380]

canvas.pack(side=TOP, padx=5, pady=5)
btn1 = Button(window, text="damier", command=draw_board)
btn1.pack(side=LEFT, padx=3, pady=3)
btn2 = Button(window, text="pions", command=draw_piece)
btn2.pack(side=RIGHT, padx=3, pady=3)

window.mainloop()
