class Triangle:
    """Cette classe implémente des triangles définis par les longueurs a, b, c de leurs trois côtés.
    """
    def __init__(self, a, b, c):
        """Constructeur de la classe.
        """
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        """Renvoie la chaîne affichée par print(t) si t est une instance de la classe Triangle.
        """
        lengths = [self.a, self.b, self.c]
        lengths.sort()
        a, b, c = tuple(lengths)
        return "Triangle de côtés {}, {}, {}".format(a, b, c)
    
    def compute_perimeter(self):    
        """Renvoie le périmètre du triangle.
        """
        return self.a + self.b + self.c

    def resize_by_factor(self, k):
        """Applique le coefficient de proportionnalité k aux trois longueurs des côtés du triangle.
        Si k > 1, le triangle est agrandit.
        Si 0 < k < 1, le trinagle est réduit.
        """
        self.a *= k
        self.b *= k
        self.c *= k

    def is_rectangle(self):
        """Renvoie un booléen indiquant si le triangle est rectangle (True) ou non (False).
        """
        lengths = [self.a, self.b, self.c]
        lengths.sort()
        a, b, c = tuple(lengths)
        return c ** 2 == a ** 2 + b ** 2

    def get_type(self):
        """Renvoie la nature (le type) du triangle sous la forme d'une chaîne : 'équilatéral', 'isocèle', 'isocèle rectangle', 'rectangle' ou 'quelconque'.
        """
        distinct_lengths = set([self.a, self.b, self.c])
        if len(distinct_lengths) == 1:
            return 'équilatéral'
        elif len(distinct_lengths) == 2:
            if self.is_rectangle():
                return 'isocèle rectangle'
            else:
                return 'isocèle'
        else:
            if self.is_rectangle():
                return 'rectangle'
            else:
                return 'quelconque'


if __name__ == "__main__":
    # On peut mettre ici quelques exemples d'utilisation de la classe Triangle pour tester sa bonne implémentation.
    pass
