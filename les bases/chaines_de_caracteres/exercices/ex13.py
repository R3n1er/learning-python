# Ordonner une chaîne de caractères

# Le but de cet exercice et de remettre en ordre alphabétique les prénoms présents 
#dans la chaîne de caractères.

chaine = "Pierre, Julien, Anne, Marie, Lucien"

chaine_liste = chaine.split(", ") # convertir la chaîne en liste en utilisant ", " comme séparateur

chaine_liste.sort() #Trier la liste

chaine_en_ordre = ", ".join(chaine_liste) # convertir la liste triée en une chaîne de caractères avec ", " comme séparateur

print(chaine_en_ordre)