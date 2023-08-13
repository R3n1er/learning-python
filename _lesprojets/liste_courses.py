
import sys
#Projet de script permettant de gérer une liste de courses
liste_courses = [] # Crée une liste vide pour stocker les éléments de la liste de courses
options = [
    "Ajouter un élément à la liste de courses",
    "Retirer un élément de la liste de courses",
    "Afficher les éléments de la liste de courses",
    "Vider la liste de courses",
    "Quitter le programme"
]

# Afficher une liste de choix possible d'actions de 1 à 5 : 
while True:
    print("Menu:")
    for i, option in enumerate(options, start=1): #Afficher toutes en options en commencant par 1
        print(f"{i}. {option}")
    choix = input("Choisissez une option de (1-5) : ") # Demander à l'utilisateur de choisir 

# Gérer le choix 1 pour ajouter un element à la liste
    if choix == "1" :
        element = input("Entrez l'élément à ajouter à la liste de courses : ")
        liste_courses.append(element) # Ajoute l'élément à la liste de courses
        print(f"L'élément {element} a été ajouté à la liste de courses.")

# Gérer le choix 2 pour supprimer un élément de la liste
    elif choix == "2" :
        if len(liste_courses) > 0 : # Vérifie si la liste de courses n'est pas vide
            print("Éléments dans la liste de courses :")
            for i, element in enumerate(liste_courses): # Afficher le contenu de la liste de courses
                print(f"{i+1}. {element}")
                #Demander à l'utilisateur le numéro d'index à retirer
            index = int(input("Entrez le numéro de l'élément à retirer : "))
            if 1 <= index and index <= len(liste_courses):  # Vérifie si le numéro de l'élément est valide
                element_retire = liste_courses.pop(index-1)  # Retire l'élément de la liste de courses
                print(f"L'élément {element_retire} a été retiré de la liste de courses.")
            else:
                print("Numéro d'élément invalide.")
        else: #gestion du cas ou la liste est vide
            print("La liste de courses est vide.")

# Gérer le choix de l'option 3 pour Afficher les éléments de la liste en cours
    elif choix == "3":
        print("Voici votre liste de courses : ")
        for i, element in enumerate(liste_courses, start=1):  # Utilisation de enumerate pour afficher l'index
            print(f"{i}. {element}")

# Gérer le choix de l'option 4 afin de vider la liste de course
    elif choix == "4":
        liste_courses.clear()
        print("La liste de courses a été vidée.")
# Gérer le choix de l'option 5 afin de quitter le programme

    elif choix == "5":
        print("Merci d'avoir utilisé la gestion de liste de courses.")
        sys.exit()
# Gérer le cas d'un choix invalide
    else:
        print("Option invalide. Veuillez choisir une option de 1 à 5.")