# Projet calculatrice avec gestion d'erreurs

# Dans ce projet, vous devez créer une calculatrice en ligne de commande qui demande à l'utilisateur de saisir deux nombres et qui affiche ensuite le résultat de l'addition de ces deux nombres. 

# Vous devez également gérer le cas de figure dans lequel l'utilisateur ne rentre pas de données valides.

while True:
    premier_nombre = input("Entrez un premier nombre : ")
    deuxieme_nombre = input("Entrez un deuxième nombre : ")

    if premier_nombre.isnumeric() and deuxieme_nombre.isnumeric():
        premier_nombre = int(premier_nombre)
        deuxieme_nombre = int(deuxieme_nombre)
        resultat = premier_nombre + deuxieme_nombre
        print(f"Le résultat de l'addition de {premier_nombre} avec {deuxieme_nombre} est égal à {resultat}")
        break
    else:
        print("Veuillez entrer deux nombres valides.")



