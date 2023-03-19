# create an empty set
# Collection non ordonnée d'éléments uniques


# Le rôle de set() est donc de créer un ensemble en prenant une collection iterable (par exemple une liste ou un tuple) en entrée 
# et en éliminant tous les doublons, pour ne garder que les éléments uniques.
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(3)

s.remove(3)
s.remove(5)

print(s)

# Imprimer dans une string formaté

print(f"The set has {len(s)} elements.")