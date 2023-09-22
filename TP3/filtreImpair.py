import os

# création des tubes nommés
if not os.path.exists("nombresImpairs"):
    os.mkfifo("nombresImpairs")
if not os.path.exists("sommeImpairs"):
    os.mkfifo("sommeImpairs")

# ouverture des tubes nommés
nombresImpairs = os.open("nombresImpairs", os.O_RDONLY)
sommeImpairs = os.open("sommeImpairs", os.O_WRONLY)

somme_impairs = 0 # initialisation de la somme des nombres impairs

while True:
    nb = int(os.read(nombresImpairs, 1024).decode().strip()) # lecture d'un nombre depuis le tube nombresImpairs
    
    if nb == -1: # si on a atteint la fin de la série de nombres impairs
        break # on sort de la boucle
    
    somme_impairs += nb # on ajoute le nombre à la somme des nombres impairs

# écriture de la somme des nombres impairs dans le tube sommeImpairs
os.write(sommeImpairs, str(somme_impairs).encode())

# fermeture des tubes nommés
os.close(nombresImpairs)
os.close(sommeImpairs)

