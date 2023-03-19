#Utilisation de map() avec lambda pour calculer le carré de chaque élément dans une liste :

nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares) # [1, 4, 9, 16, 25]
