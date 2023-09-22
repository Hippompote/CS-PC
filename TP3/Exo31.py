import sys,os,multiprocessing,random
dfr1, dfw1 = multiprocessing.Pipe() #tubeNpair
dfr2, dfw2 = multiprocessing.Pipe() #tubeNimpair
dfr3, dfw3 = multiprocessing.Pipe() #tubeSommePair
dfr4, dfw4 = multiprocessing.Pipe() #tubeSommeImpair

sP=0
sI=0
stopP=0
stopI=0

N = int(sys.argv[1])


if os.fork() == 0:
    for i in range(N):
        x = random.randint(0,100)
        if x%2 == 0:
            dfw1.send(x)
        else:
            dfw2.send(x)
    dfw1.send(-1)
    dfw2.send(-1)
    print("Somme des nombres pair : "+str(dfr3.recv()))
    print("Somme des nombres impair : "+str(dfr4.recv()))

else:
    if os.fork()==0:
        while stopP != -1:
            Np = dfr1.recv()
            if Np == -1:
                stopP = -1
            else:
                sP += Np
        dfw3.send(sP)
    else:
        while stopI != -1:
            Ni = dfr2.recv()
            if Ni == -1:
                stopI = -1
            else:
                sI += Ni
        dfw4.send(sI)
