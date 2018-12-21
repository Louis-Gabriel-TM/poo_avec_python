from tkinter import Button, Canvas, Tk, LEFT, BOTTOM
from random import choice


def draw_line():
    global y1, y2
    canvas.create_line(x1, y1, x2, y2, width=2, fill=color)
    y1 -= 10
    y2 += 10


def draw_line2():
    """Trace deux lignes rouges se croisant au centre du canevas,
    l'une horizontale et l'autre verticale, pour former un "viseur".
    """
    canvas.create_line(0, 325, 499, 325, width=2, fill='red')
    canvas.create_line(250, 0, 250, 649, width=2, fill='red')


def change_color():
    global color
    color_palette = [
        'purple', 'cyan', 'brown', 'green', 'red', 'blue', 'orange', 'yellow'
    ]
    color = choice(color_palette)


x1, y1 = 0, 640
x2, y2 = 499, 10
color = 'dark green'

window = Tk()

canvas = Canvas(window, bg='dark grey', height=650, width=500)
canvas.pack(side=LEFT)

btn1 = Button(window, text="Quitter", command=window.quit)
btn1.pack(side=BOTTOM)

btn2 = Button(window, text="Tracer une ligne", command=draw_line)
btn2.pack()
btn3 = Button(window, text="Autre couleur", command=change_color)
btn3.pack()

"""
Ajout du bouton faisant apparaître le "viseur".
"""
btn4 = Button(window, text="Viseur", command=draw_line2)
btn4.pack()

window.mainloop()

window.destroy()
