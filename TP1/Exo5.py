import os,sys

pid1 = os.fork()
if pid1==0:
    for i in range(1,51):
        print(i)
else:
    pid2 = os.fork()
    if pid2 ==0:
        for i in range(51,101):
            print(i)
        else:
            os.waitpid(pid1,0)
            os.waitpid(pid2,0)