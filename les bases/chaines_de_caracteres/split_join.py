#manipulation de chaines de caractères
chaine = "1, 2, 3, 4, 5"

print(chaine)

print("> Utilisation de la methode split")

print(chaine.split(", "))

print("> Utilisation de la methode join")

print(", ".join(chaine.split(", ")))

print(".".join(chaine.split(", ")))