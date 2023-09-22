import os,sys

for i in range(3):
    pid = os.fork()
    f = os.getpid()
    p = os.getppid()
    print(f"i:{i}: je suis le processus {f}, mon daron c'est le processus {p}, retour:{pid}")
    
print("Fin du programme")
