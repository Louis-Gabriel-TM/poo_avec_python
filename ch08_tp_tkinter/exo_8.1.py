from tkinter import Button, Canvas, Tk, LEFT, BOTTOM
from random import choice


def draw_line():
    global y1, y2
    canvas.create_line(x1, y1, x2, y2, width=2, fill=color)
    y1 -= 10
    y2 += 10


def change_color():
    global color

    """
    Il suffit ici de restreindre la palette aux trois couleurs retenues...
    """
    color_palette = [
        'cyan', 'brown', 'green'
    ]
    color = choice(color_palette)


x1, y1 = 10, 390
x2, y2 = 390, 10

"""
... sans oublier de fixer la couleur initiale dans cette palette restreinte.
"""
color = 'cyan'

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
