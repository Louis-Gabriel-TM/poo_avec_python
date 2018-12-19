from tkinter import Button, Canvas, Tk, ARC, LEFT, BOTTOM


def draw_circle(x0, y0, radius, color):
    """Trace un cercle de centre (x0, y0), de rayon 'radius' et de couleur 'color'.
    Le paramètre 'style' fixé sur ARC indique que l'on souhaite un arc de cercle et non un secteur de disque.
    Le paramètre 'outline' donne la couleur du cercle (la bordure du disque).
    """
    canvas.create_arc(
        x0 - radius, y0 - radius, x0 + radius, y0 + radius,
        start=0, extent=359.9, width=8, style=ARC, outline=color
    )


def africa():
    draw_circle(320, 180, 50, 'black')


def america():
    draw_circle(440, 180, 50, 'red')


def asia():
    draw_circle(260, 220, 50, 'yellow')


def europa():
    draw_circle(200, 180, 50, 'blue')


def oceania():
    draw_circle(380, 220, 50, 'green')


window = Tk()

canvas = Canvas(window, bg='grey', width=640, height=400)
canvas.pack(side=LEFT)

canvas.create_rectangle(50, 40, 590, 360, fill='white')

btn_quit = Button(window, text="Quitter", command=window.quit)
btn_quit.pack(side=BOTTOM)

btn_europa = Button(window, text="Europe", command=europa)
btn_europa.pack()
btn_africa = Button(window, text="Afrique", command=africa)
btn_africa.pack()
btn_america = Button(window, text="Amériques", command=america)
btn_america.pack()
btn_asia = Button(window, text="Asie", command=asia)
btn_asia.pack()
btn_oceania = Button(window, text="Océanie", command=oceania)
btn_oceania.pack()

window.mainloop()

window.destroy()
