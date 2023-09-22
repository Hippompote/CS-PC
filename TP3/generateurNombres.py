import random
import os
import sys

# création des tubes nommés
if not os.path.exists("nombresPairs"):
    os.mkfifo("nombresPairs")
if not os.path.exists("nombresImpairs"):
    os.mkfifo("nombresImpairs")
if not os.path.exists("sommePairs"):
    os.mkfifo("sommePairs")
if not os.path.exists("sommeImpairs"):
    os.mkfifo("sommeImpairs")

# ouverture des tubes nommés
nombresPairs = os.open("nombresPairs", os.O_WRONLY)
nombresImpairs = os.open("nombresImpairs", os.O_WRONLY)
sommePairs = os.open("sommePairs", os.O_RDONLY)
sommeImpairs = os.open("sommeImpairs", os.O_RDONLY)

N = sys.argv[1] # nombre de nombres aléatoires à générer
somme_pairs = 0 
somme_impairs = 0 

for i in range(N):
    nb = random.randint(0, 100) # génération d'un nombre aléatoire entre 0 et 100
    
    if nb % 2 == 0: # si le nombre est pair
        os.write(nombresPairs, str(nb).encode()) # on l'écrit dans le tube nombresPairs
        somme_pairs += nb 
    else: 
        os.write(nombresImpairs, str(nb).encode()) 
        somme_impairs += nb 

os.write(nombresPairs, str(-1).encode()) 
os.write(nombresImpairs, str(-1).encode()) 

# lecture des deux nombres stockés dans les tubes sommePairs et sommeImpairs
somme_pairs_tube = int(os.read(sommePairs, 1024).decode().strip())
somme_impairs_tube = int(os.read(sommeImpairs, 1024).decode().strip())

# affichage du résultat
print("La somme totale des nombres pairs  est :", somme_pairs_tube)
print("La somme totale des nombres impairs  est :", somme_impairs_tube)

# fermeture des tubes nommés
os.close(nombresPairs)
os.close(nombresImpairs)
os.close(sommePairs)
os.close(sommeImpairs)

