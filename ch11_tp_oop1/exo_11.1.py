class Point:
    """Classe modélisant des points dans un espace à deux dimensions.
    """
    def __init__(self, x, y):
        """x et y sont respectivement l'abscisse et l'ordonnée du point.
        """
        self.x = x
        self.y = y

def distance(p1, p2):
    """Le théorème de Pythagore indique que, dans un repère orthonormé, la longueur d'un vecteur de coordonnées (X, Y) est la racine carrée de 
    X ** 2 + Y ** 2.
    p2.x - p1.x donne l'abscisse du vecteur allant de p1 vers p2.
    p2.y - p1.y donne l'abscisse du vecteur allant de p1 vers p2.
    """
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5


if __name__ == '__main__':
    """Test s'appuyant sur le triplet pythagoricien (3, 4, 5) :
    3 ** 2 + 4 ** 2 = 5 ** 2
    La distance séparant (0, 3) et (4, 0) vaut 5.
    """
    point1 = Point(0, 3)
    point2 = Point(4, 0)
    print(distance(point1, point2))