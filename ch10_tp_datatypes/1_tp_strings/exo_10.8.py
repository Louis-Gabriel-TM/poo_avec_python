sentence = "Noël n'est pas en été, benêt !"

count = 0  # On peut par exemple initialiser un compteur...

for c in sentence:  # ... puis parcourir la phrase caractère par caractère.
    # Regarder si le caractère est dans une chaîne formée des caractères recherchés...
    if c in "eéèêë":
        print(c)
        count += 1  # ... et dans ce cas incrémenter le compteur

print(count)
