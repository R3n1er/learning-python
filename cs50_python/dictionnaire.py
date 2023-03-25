#Déclaration d'un dictionnaire
infos_labradoodle = {}

infos_labradoodle = {
    "poids" : "13 à 16 kg",
    "origine" : "Etats-Unis"
}

#Ajouter une nouvelle clé-valeur au dictionnaire
infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"

print(infos_labradoodle)


#supprimer une pair clé-valeur
del infos_labradoodle["origine"]
print(infos_labradoodle)

# Vérifier l'existence d'un mot clé spécifique 