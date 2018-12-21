nb = [5, 3, 1, 5, 4, 4, 2, 3]

"""On va transformer cette liste en un ensemble, un 'set'. Il s'agit d'un type de données "built-in" au même titre que les listes ou les tuples.
Un 'set' ne comporte pas de doublon et ses éléments ne sont pas repérés par des indices. Les éléments sont considérés comme n'étant pas ordonnés et un 'set' ne peut être trié.
"""
values_set = set(nb)  # nb_set = {1, 2, 3, 4, 5}

# Maintenant que les doublons ont disparu, revenons à une liste...
values_list = list(values_set)

values_list.sort()

print("Liste initiale >>>", nb)
print("Liste sans doublon et triée >>>", values_list)
