import signal
import sys
import time

def signal_handler(sig, frame):
    print("Signal SIGINT reçu, arrêt du programme...")
    sys.exit(0)

# définir la fonction d'interception de signal pour SIGINT
signal.signal(signal.SIGINT, signal_handler)

# boucle infinie
while True:
    time.sleep(1)
    print("Boucle infinie en cours...")
