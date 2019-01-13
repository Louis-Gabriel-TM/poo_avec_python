### Exemple de la balle animée ###


from tkinter import Button, Canvas, Tk, BOTTOM, LEFT


def move_ball():
    """Déplace la balle selon le vecteur de coordonnées (dx, dy).
    """
    global x, y, dx, dy
    x += dx
    y += dy

    if x > 420:  # si la balle atteint le côté droit, ...
        x = 420
        dx, dy = 0, 30  # ... elle se met à descendre

    if y > 420:  # si la balle atteint le bas du canevas, ...
        y = 420
        dx, dy = -30, 0  # ... elle continue vers la gauche

    if x < 20:  # si la balle atteint le côté gauche, ...
        x = 20
        dx, dy = 0, -30  # ... elle se met à remonter

    if y < 20:  # si la balle atteint le haut du canevas, ...
        y = 20
        dx, dy = 30, 0  # ... elle continue vers la droite

    canvas.coords(ball, x, y, x + 60, y + 60)

    if animate:
        window.after(50, move_ball)  # on met en pause 50 ms avant de reprendre

def start_ball():
    """Démarre l'animation.
    """
    global animate
    if not animate:
        animate = True
        move_ball()

def stop_ball():
    """Arrête l'animation.
    """
    global animate
    animate = False


##### Programme principal #####

x, y = 20, 20  # position intiale de la balle
dx, dy = 30, 0  # pas horizontal et vertical du déplacement
animate = False  # variable autorisant ou non l'animation

# Création de la fenêtre et de ses widgets
window = Tk()
window.title("Exemple d'animantion avec tkinter")

canvas = Canvas(window, width=500, height=500)
canvas.pack(side=LEFT, padx=5, pady=5)

ball = canvas.create_oval(x, y, x + 60, y + 60, width=2, fill='red')

btn_quit = Button(window, text="Quitter", width=8, command=window.quit)
btn_quit.pack(side=BOTTOM)

btn_start = Button(window, text="Démarrer", width=8, command= start_ball)
btn_start.pack()

btn_stop = Button(window, text="Arrêter", width=8, command=stop_ball)
btn_stop.pack()

window.mainloop()