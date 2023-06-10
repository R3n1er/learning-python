# Dans cet exercice, vous allez devoir afficher les lettres d'un mot dans l'ordre inverse, lettre par lettre, grâce à une boucle.


#Utiliser la fonction reversed()

# Demander à l'utilisateur de saisir un mot
mot = input("Saisissez un mot : ")

# Mettre ce mot à l'envers
mot_inverse = "".join(reversed(mot))

# Afficher à la ligne chaque lettre du nouveau mot à l'envers
for lettre in mot_inverse:
    print(lettre)