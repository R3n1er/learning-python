import random


def jeu_devine():
    nombre_mystere = random.randint(0, 100)

    print("Bienvenue dans le jeu de devinette !")
    print("Je pense à un nombre entre 0 et 100. À vous de deviner.")

    essais_restants = 5

    while essais_restants > 0:
        # Demander à l'utilisateur de deviner
        try:
            essai = int(input("Entrez votre nombre : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if essai == nombre_mystere:
            print(
                f"Félicitations ! Vous avez trouvé le nombre mystère {nombre_mystere} en {5 - essais_restants + 1} essais.")
            break
        elif essai < nombre_mystere:
            print("Non, le nombre mystère est plus grand.")
        else:
            print("Non, le nombre mystère est plus petit.")

        essais_restants -= 1

    if essais_restants == 0:
        print(
            f"Désolé, vous avez épuisé vos essais. Le nombre mystère était {nombre_mystere}.")


jeu_devine()
