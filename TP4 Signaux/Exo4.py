import os,sys,time,signal
N = 6
j = 0
pid = os.fork()

if pid ==0:
    while True:
        time.sleep(2)
        print("Bonsoir je fils",j)
        j+=1
else:
    for i in range(N):
        time.sleep(2)
        print(i)
        if i == 3:
            os.kill(pid,signal.SIGKILL)