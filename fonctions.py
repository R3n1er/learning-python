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
# if-else
x = 10
if x > 0:
    print("x est positif")
elif x == 0:
    print("x est nul")
else:
    print("x est négatif")

# Boucle for
for i in range(5):
    print(i)

# Boucle while
i = 0
while i < 5:
    print(i)
    i += 1
