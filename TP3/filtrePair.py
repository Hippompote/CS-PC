import os

# création des tubes nommés
if not os.path.exists("nombresPairs"):
    os.mkfifo("nombresPairs")
if not os.path.exists("sommePairs"):
    os.mkfifo("sommePairs")

# ouverture des tubes nommés
nombresPairs = os.open("nombresPairs", os.O_RDONLY)
sommePairs = os.open("sommePairs", os.O_WRONLY)

somme_pairs = 0 # initialisation de la somme des nombres pairs

while True:
    nb = int(os.read(nombresPairs, 1024).decode().strip()) # lecture d'un nombre depuis le tube nombresPairs
    
    if nb == -1: # si on a atteint la fin de la série de nombres pairs
        break # on sort de la boucle
    
    somme_pairs += nb # on ajoute le nombre à la somme des nombres pairs

# écriture de la somme des nombres pairs dans le tube sommePairs
os.write(sommePairs, str(somme_pairs).encode())

# fermeture des tubes nommés
os.close(nombresPairs)
os.close(sommePairs)
