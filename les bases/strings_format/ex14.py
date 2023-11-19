# Créer une chaîne de caractères avec une f-string
# Dans cet exercice, vous devez recréer l'URL du site https://www.docstring.fr/glossaire/ grâce 
# aux différents variables et à l'aide d'une f-string.
# 


# Ne modifiez pas les variables ci-dessous
protocole = "https://"
nom_du_site = "docstring"
extension = "fr"
page = "glossaire"

# Modifiez le code à partir d'ici 
URL = f"{protocole}www.{nom_du_site}.{extension}/{page} "

print(URL)