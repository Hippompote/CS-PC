import signal
import sys
import time
global fin
fin = False

def signal_handler(sig, frame):
    print("Signal SIGINT reçu, arrêt du programme...")
    sys.exit(0)

def ignore(sig,frame):
    print('ya R')
# définir la fonction d'interception de signal pour SIGINT

def launch(sig,frame):
    global fin
    fin = True
    return fin


signal.signal(signal.SIGINT, launch)

# boucle infinie
while fin == False:
    time.sleep(1)
    print("Boucle infinie en cours...")