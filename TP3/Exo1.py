import os

# Créer le tube anonyme (pipe)
rfd, wfd = os.pipe()

pid = os.fork()

if pid == 0:
    # Dans le processus enfant, fermer le descripteur de lecture
    os.close(rfd)
    
    # Écrire des données dans le tube anonyme
    message = "Hello, parent process!"
    os.write(wfd, message.encode())
    
    # Fermer le descripteur d'écriture
    os.close(wfd)
else:
    # Dans le processus parent, fermer le descripteur d'écriture
    os.close(wfd)
    
    # Lire des données depuis le tube anonyme
    message = os.read(rfd, 100)
    print("Message reçu du processus enfant: ", message.decode())
    
    # Fermer le descripteur de lecture
    os.close(rfd)
