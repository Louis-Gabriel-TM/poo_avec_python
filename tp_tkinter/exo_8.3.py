from tkinter import Button, Canvas, Tk, LEFT, BOTTOM
from random import choice


def draw_line():
    global y1, y2
    canvas.create_line(x1, y1, x2, y2, width=2, fill=color)
    y1 -= 10
    y2 += 10


def change_color():
    global color
    color_palette = [
        'purple', 'cyan', 'brown', 'green', 'red', 'blue', 'orange', 'yellow'
    ]
    color = choice(color_palette)


"""
Pour que les lignes atteignent le bord du canevas, il faut que les 
abscisses x1 et x2 prennent les valeurs min et max de ce canevas, 
soit 0 et 499 pour une largeur de 500 (en ajustant également y1 et y2
si on veut conserver des lignes "centrées")...
"""
x1, y1 = 0, 640
x2, y2 = 499, 10
color = 'dark green'

window = Tk()

"""
... dimensions du canevas qu'il faut modifier à la création / initialisation
de celui-ci.
"""
canvas = Canvas(window, bg='dark grey', height=650, width=500)
canvas.pack(side=LEFT)

btn1 = Button(window, text="Quitter", command=window.quit)
btn1.pack(side=BOTTOM)

btn2 = Button(window, text="Tracer une ligne", command=draw_line)
btn2.pack()
btn3 = Button(window, text="Autre couleur", command=change_color)
btn3.pack()

window.mainloop()

window.destroy()
