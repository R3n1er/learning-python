# Fonction qui calcul le factoriel d'un nombre
def calculer_factoriel(nombre):
    if nombre == 0:
        return 1
    else:
        return nombre * calculer_factoriel(nombre - 1)

# Exemple d'utilisation
resultat = calculer_factoriel(5)
print(resultat)

