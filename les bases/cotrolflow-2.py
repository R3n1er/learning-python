# voici un code qui affiche un message différent en fonction de l'heure actuelle :
# si l'heure actuelle est inférieure à 12 heures, le programme affichera "Bonjour !", sinon il affichera "Bon après-midi !".
import datetime

heure_actuelle = datetime.datetime.now().hour

if heure_actuelle < 12:
    print("Bonjour !")
else:
    print("Bon après-midi !")
