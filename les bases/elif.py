statut_commande = "expédiée"

if statut_commande == "en attente":
    print("Votre commande est en attente de traitement.")
elif statut_commande == "en cours":
    print("Votre commande est en cours de préparation.")
elif statut_commande == "expédiée":
    print("Votre commande a été expédiée. Elle devrait arriver bientôt.")
else:
    print("Désolé, nous ne reconnaissons pas le statut de votre commande.")
