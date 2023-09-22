import sys,os

def fontion():
    os.fork()
    print("Hello World !")
    os.fork()
    os.fork()

fontion()
print('Hello World !')
sys.exit(0)