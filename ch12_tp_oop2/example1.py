# coding: utf-8

# Exemple d'une classe 'Ion' héritant d'une classe 'Atom'

class Atom:  # 'Atom' hérite implicitement de la classe fondamentale 'Object'
    """Classe modélisant les 10 premiers éléments de la table de Mendeleïev (ou tableau périodique des éléments).
    """
    # Le début de la table de Mendeleïev est mis en attribut de classe
    table = [
        None,
        ("hydrogène", 0),  # (nom de l'élément, nombre de neurons de l'élément)
        ("hélium", 1),
        ("lithium", 4),
        ("béryllium", 5),
        ("bore", 6),
        ("carbone", 6),
        ("azote", 7),
        ("oxygène", 8),
        ("fluor", 10),
        ("néon", 10)
    ]

    def __init__(self, atomic_nb):
        """Le numéro atomique 'atomic_nb' détermine le nombre de protons et d'électrons.
        Le nombre de neutrons provient de l'attribut de classe 'table'.
        """
        self.protons_nb = atomic_nb
        self.electrons_nb = atomic_nb
        self.neutrons_nb = Atom.table[atomic_nb][1]  # un attribut de classe est préfixé par le nom de la classe

    def __str__(self):
        atom_str = """
            Nom de l'élément : {0}
            {1} protons, {2} électrons, {3} neutrons""". format(
                Atom.table[self.protons_nb][0].capitalize(),
                self.protons_nb,
                self.electrons_nb,
                self.neutrons_nb
            )
        return atom_str

class Ion(Atom):  # La classe 'Ion' hérite de la classe 'Atom'
    """On considère ici que les ions sont des atomes ayant gagné ou perdu des électrons.
    Contrairement aux atomes purs, ils ne sont plus électriquement neutres et possèdent une charge électrique.
    """
    def __init__(self, atomic_nb, electrical_charge):  # on "surcharge" ici le constructeur de la classe 'Atom'
        """Le numéro atomique et la charge électrique détermine la nature de l'ion.
        """
        Atom.__init__(self, atomic_nb)  # un ion est un atome...
        self.charge = electrical_charge  # ... avec un attribut en plus...
        self.electrons_nb -= electrical_charge  # ... et un attribut ajusté

    def __str__(self):
        formated_str = Atom.__str__(self)  # on récupère la chaîne formatée pour afficher une instance de la classe 'Atom'...
        formated_str += """
            Particule électrisée de charge {}""".format(
                self.charge
            )  # ...et on y ajoute une information supplémentaire
        return formated_str


if __name__ == "__main__":
    print("\nTest pour un atome de Bore :")
    atom1 = Atom(5)
    print(atom1)

    print("\nTest pour un ion Lithium de charge + 1 :")
    ion1 = Ion(3, 1)
    print(ion1)

    print("\nTest pour un ion Oxygène de charge - 2 :")
    ion2 = Ion(8, -2)
    print(ion2)
    