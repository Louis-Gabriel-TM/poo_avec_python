from math import log10
from tkinter import Button, Canvas, Entry, Label, Tk


class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title("Code des couleurs")

        self.draw_resistor()

        Label(
            self.root, text="Entrez la valeur de la résisitance, en ohms :"
        ).grid(row=2, column=1, columnspan=3)

        # le bouton 'Montrer' a été supprimé...

        Button(
            self.root, text="Quitter", command=self.root.quit
        ).grid(row=3, column=3)

        self.input_zone = Entry(self.root, width=28)
        self.input_zone.grid(row=3, column=2)

        # ... et l'apparition des bandes de couleur sera désormais gérée par la touche <Retur>, attachée à la zone de saisie avec la méthode 'bind' de la classe 'Entry'
        self.input_zone.bind(sequence='<Return>', func=self.change_colors)

        self.color_code = [
            'black', 'brown', 'red', 'orange', 'yellow',
            'green', 'blue', 'purple', 'grey', 'white'
        ]

        self.root.mainloop()

    def draw_resistor(self):
        self.canvas = Canvas(self.root, width=500, height=200, bg='ivory')
        self.canvas.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        self.canvas.create_line(20, 100, 480, 100, width=5)
        self.canvas.create_rectangle(
            130, 60, 370, 140, fill='light grey', width=3
        )

        self.strips = []
        for x in range(170, 300, 48):
            self.strips.append(
                self.canvas.create_rectangle(
                    x, 62, x + 24, 139, fill='black', width=0
                )
            )

    def change_colors(self, id):  # un identifiant est renvoyé par 'bind' à la fonction appelée et doit donc est pris en compte dans les paramètres de cette fonction appelée (même si, comme ici, il ne sera pas exploité)
        self.user_input = self.input_zone.get()

        try:
            value = int(self.user_input)
        except:
            error_code = 1
        else:
            error_code = 0

        if error_code == 1 or value < 10 or value > 1e11:
            self.raise_error()
        else:
            codes = [0, 0, 0]
            max_exponent = int(log10(value))
            magnitude_order = 10 ** max_exponent
            codes[0] = int(value / magnitude_order)
            decimal_part = value / magnitude_order - codes[0]
            codes[1] = int(decimal_part * 10 + 0.5)
            codes[2] = max_exponent - 1
            for n in range(3):
                self.canvas.itemconfigure(
                    self.strips[n], fill=self.color_code[codes[n]]
                )

    def raise_error(self):
        self.input_zone.configure(bg='red')
        self.root.after(1000, self.clear_input_zone)

    def clear_input_zone(self):
        self.input_zone.configure(bg='white')
        self.input_zone.delete(0, len(self.user_input))

        # en cas de saisie incorrecte, il faut maintenant que les trois bandes redeviennent noires
        for n in range(3):
            self.canvas.itemconfigure(
                self.strips[n], fill='black'
            )


if __name__ == '__main__':
    app = Application()
