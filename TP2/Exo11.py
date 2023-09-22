import os

# Fonction pour le premier processus
def process1():
    print("Processus 1 en cours d'exécution")

# Fonction pour le deuxième processus
def process2():
    print("Processus 2 en cours d'exécution")

# Lancer le premier processus
pid1 = os.fork()
if pid1 == 0:
    process1()
else:
    # Lancer le deuxième processus
    pid2 = os.fork()
    if pid2 == 0:
        process2()
    else:
        # Attendre que les deux processus se terminent
        os.waitpid(pid1, 0)
        os.waitpid(pid2, 0)
        print("Les deux processus sont terminés")
