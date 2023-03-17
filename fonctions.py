# Fonction simple
def dire_bonjour(nom):
    print("Bonjour", nom)

# Appel de fonction
dire_bonjour("Alice")

# Fonction avec retour de valeur
def addition(a, b):
    return a + b

# Appel de fonction avec retour de valeur
resultat = addition(5, 3)
print("5 + 3 =", resultat)

# Fonction qui calcule la somme de 2 nombres
def calculer_somme(nombre1, nombre2):
    somme = nombre1 + nombre2
    return somme

# Exemple d'utilisation
resultat = calculer_somme(3, 5)
print(resultat)
