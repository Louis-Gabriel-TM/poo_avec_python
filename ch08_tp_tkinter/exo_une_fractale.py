# Exercice (diaporama) : une fractale

from random import choice, randrange
from tkinter import Button, Canvas, Tk, ALL, LEFT, TOP


def plot(x, y):
    """Représente le point de coordonnées (x, y) par une petit disque de centre (x, y) et de rayon 2px.
    """
    canvas.create_oval(
        x - 1, y - 1, x + 1, y + 1, fill='black'
    )

def init_vertex():
    global vertex
    canvas.delete(ALL)
    vertex = []
    for _ in range(3):
        x = randrange(600)
        y = randrange(600)
        vertex.append((x, y))
        plot(x, y)

def plot_process():
    pt1 = choice(vertex)
    for _ in range(50):
        pt2 = choice(vertex)
        middle = [
            (pt1[0] + pt2[0]) // 2,
            (pt1[1] + pt2[1]) // 2
        ]
        plot(middle[0], middle[1])
        #canvas.update_idletasks()
        pt1 = middle

### Programme principal ###

# On créé une liste destinée à recueillir les trois sommets
vertex = []

# On créé la fenêtre, la zone de dessin et les deux boutons
window = Tk()
window.title("Triangle de Sierpinski")
canvas = Canvas(window, width=600, height=600, bg='ivory')
canvas.pack(side=TOP, padx=5, pady=5)
btn_init = Button(window, text="Init", command=init_vertex)
btn_init.pack(side=LEFT, padx=5, pady=5)
btn_go = Button(window, text="50 iterations", command=plot_process)
btn_go.pack(side=LEFT, padx=5, pady=5)
btn_quit = Button(window, text="Quit", command=window.quit)
btn_quit.pack(side=LEFT, padx=5, pady=5)

# Lancement du réceptionnaire d'événements de la fenêtre
window.mainloop()
