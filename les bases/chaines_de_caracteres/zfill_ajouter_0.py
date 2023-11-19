#Utilisation de la methode zfill
#Pratique quand on utilise des séquences 

#S'utilise uniquement sur des chaines de caractères

print("9".zfill(4))

#Application de Zfill dans une boucle
print(">Application de Zfill dans une boucle")

for i in range(10):
    print(str(i).zfill(4))