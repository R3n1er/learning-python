#Instructions conditionnelles
age = 25
if age < 18:
    print("Vous êtes mineur.")
elif age >= 18 and age < 65:
    print("Vous êtes majeur.")
else:
    print("Vous êtes retraité.")

# La boucle for
for i in range(5):
    print(i)
# Dans cet exemple, nous avons utilisé la boucle for pour afficher les nombres de 0 à 4. La fonction range(5) renvoie une séquence de nombres allant de 0 à 4, et la boucle for itère sur chaque nombre et l'affiche à l'écran.

# La boucle While
# Le code suivant calcule la somme des nombres de 1 à 10
somme = 0
i = 1

while i <= 10:
    somme += i
    i += 1

print("La somme est", somme)


#Les expressions booléennes
a = 5
b = 10
c = 15

print(a < b)    # True
print(a > b)    # False
print(b >= c)   # False
print(a == 5 and b == 10)   # True
print(a == 5 or b == 15)    # True
print(not a == 5)   # False



