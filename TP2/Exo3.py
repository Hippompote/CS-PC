import os

# Fork pour exécuter les commandes simultanément en parallèle avec le séparateur &
pid = os.fork()

if pid == 0:
    # Processus fils pour la commande "who"
    print("Exécution de la commande who sim")
    os.execlp("who", "who")
else:
    # Fork pour la commande "ps"
    pid = os.fork()
    
    if pid == 0:
        # Processus fils pour la commande "ps"
        print("Exécution de la commande ps sim")
        os.execlp("ps", "ps")
    else:
        pid = os.fork()
        if pid ==0:
        # Commande "ls -l"
            print("Exécution de la commande ls sim")
            os.execlp("ls", "ls", "-l")

# Attente de la fin de tous les processus enfants
for i in range(2):
    os.wait()

# Fork pour exécuter les commandes successivement séquentiellement avec le séparateur ;
pid = os.fork()

if pid == 0:
    # Processus fils pour la commande "who"
    print("Exécution de la commande who séq")
    os.execlp("who", "who")
else:
    # Attente de la fin du processus "who" avant de continuer
    os.wait()
    # Fork pour la commande "ps"
    pid = os.fork()
    
    if pid == 0:
        # Processus fils pour la commande "ps"
        print("Exécution de la commande ps séq")
        os.execlp("ps", "ps")
    else:
        # Attente de la fin du processus "ps" avant de continuer
        os.wait()
        # Commande "ls -l"
        pid = os.fork()
        if pid ==0:
            print("Exécution de la commande ls séq")
            os.execlp("ls", "ls", "-l")
        
# Attente de la fin de tous les processus enfants
for i in range(2):
    os.wait()
