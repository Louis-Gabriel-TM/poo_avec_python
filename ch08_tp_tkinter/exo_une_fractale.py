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
    """Vide la liste 'vertex' (globale) et y place trois nouveaux sommets dont les coordonnées (x, y) ont été fixées de manière aléatoire.
    La zone de dessin est effacée au passage.
    """
    # On importe une variable globale pour la modifier : c'est mal :-p
    global vertex
    # On efface la zone de dessin...
    canvas.delete(ALL)
    # ... et on vide la liste des sommets
    vertex = []

    for _ in range(3):
        x = randrange(600)  # randrange(600) renvoie un entier entre 0 et 599 inclus
        y = randrange(600)
        vertex.append((x, y))  # on ajoute un sommet (x, y) à la liste...
        plot(x, y)  # ... et on l'affiche

def plot_process():
    """Effectue 50 itérations de la boucle décrite dans l'énoncé.
    """
    pt1 = choice(vertex)  # 'choice' prend un élément au hasard dans la liste 'vertex'
    for _ in range(50):
        pt2 = choice(vertex)
        # on calcule les coordonnées du milieu du segment joignant 'pt1' à 'pt2'
        middle = [
            (pt1[0] + pt2[0]) // 2,
            (pt1[1] + pt2[1]) // 2
        ]
        plot(middle[0], middle[1])
        #canvas.update_idletasks()
        pt1 = middle  # on va utiliser ce milieu comme point de départ pour le prochain tour de boucle

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
