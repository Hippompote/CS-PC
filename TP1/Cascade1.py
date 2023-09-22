import os,sys

N = int(input("Entrez un nombre de processus à réaliser:"))  # nombre de processus à créer

for i in range(2, N+1):
    # Création des processus P2, P3, ..., PN
    pid = os.fork()
    if pid != 0:  # code exécuté par le père
        print(f"Je suis le processus père (PID = {os.getpid()})")
        sys.exit(0)
    else:  # code exécuté par le fils
        print(f"Je suis le processus fils (PID = {os.getpid()})")