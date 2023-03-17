# Fonction qui trouve le plus grand nombre dans une liste :

def trouver_max(liste):
    max = liste[0]
    for nombre in liste:
        if nombre > max:
            max = nombre
    return max

# Exemple d'utilisation
ma_liste = [3, 5, 1, 8, 2]
resultat = trouver_max(ma_liste)
print(resultat)
