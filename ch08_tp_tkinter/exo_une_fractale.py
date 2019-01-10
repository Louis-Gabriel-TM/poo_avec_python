# Exercice (diaporama) : une fractale

from tkinter import Button, Canvas, Tk, LEFT, TOP


def plot(x, y):
    """Représente le point de coordonnées (x, y) par une petit disque de centre (x, y) et de rayon 2px.
    """
    canvas.create_oval(
        x - 1, y - 1, x + 1, y + 1, fill='black'
    )


def init_vertex():
    pass


def plot_process():
    pass


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
btn_go = Button(window, text="Go", command=plot_process)
btn_go.pack(side=LEFT, padx=5, pady=5)

# Lancement du réceptionnaire d'événements de la fenêtre
window.mainloop()
