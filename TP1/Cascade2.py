import os,sys

N = int(input("Entrez un nombre de processus à réaliser:"))  # nombre de processus à créer

for i in range(2,N+1):
    pid = os.fork()
    if pid !=0: #Code éxécuté par le père
        print(f"Je suis le processus père (PID = {os.getpid()})")
    else: #Code éxécuté par le fils
        print(f"Je suis le processus fils (PID = {os.getpid()})")
        sys.exit(0)