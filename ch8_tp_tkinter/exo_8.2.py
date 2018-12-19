from tkinter import Button, Canvas, Tk, LEFT, BOTTOM
from random import choice

"""
Les lignes sont horizontales si les ordonnées y1 et y2
sont identiques...
"""


def draw_line():
    global y1, y2
    canvas.create_line(x1, y1, x2, y2, width=2, fill=color)

    """
    ... donc y1 et y2 doivent être modifiés de la même façon...
    """
    y1 += 10
    y2 += 10


def change_color():
    global color
    color_palette = [
        'purple', 'cyan', 'brown', 'green', 'red', 'blue', 'orange', 'yellow'
    ]
    color = choice(color_palette)


"""
... sans oublier de donner à y1 et y2 la même valeur initiale.
"""
x1, y1 = 10, 10
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
