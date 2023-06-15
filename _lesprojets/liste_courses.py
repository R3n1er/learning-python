

#Projet de script permettant de gérer une liste de courses
liste_courses = [] # Crée une liste vide pour stocker les éléments de la liste de courses
# Afficher une liste de choix possible d'actions de 1 à 5 : 
while True:
    print("Menu:")
    print("1. Ajouter un élément à la liste de courses")
    print("2. Retirer un élément de la liste de courses")
    print("3. Afficher les éléments de la liste de courses")
    print("4. Vider la liste de courses")
    print("5. Quitter le programme")
    choix = input("Choisissez une action (1-5) : ") # Demander à l'utilisateur de choisir 

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
            index = int(input("Entrez le numéro de l'élément à retirer : "))
            if 1 <= index <= len(liste_courses):  # Vérifie si le numéro de l'élément est valide
                element_retire = liste_courses.pop(index-1)  # Retire l'élément de la liste de courses
                print(f"L'élément {element_retire} a été retiré de la liste de courses.")
            else:
                print("Numéro d'élément invalide.")
        else: #gestion du cas ou la liste est vide
            print("La liste de courses est vide.")
