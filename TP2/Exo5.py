import sys,os,time

N = int(sys.argv[1])
for i in range(N):
    pid = os.fork()
    if pid==0:
        print(f'pid: {os.getpid()}, père: {os.getppid()}')
        time.sleep(2*i)
        sys.exit(i)
    else:
        pid_fils,etat = os.wait()
        print(f'pid du fils:{pid_fils}')
        print(f'etat:{etat}')