#!/data/user/0/ru.iiec.pydroid3/files/x86_64-linux-android/bin/python3

N = input()
nP = 0
nM = 0

for Ti in range(int(N)):
    Ti = int(input())
    
    if Ti == 1:
        nP = nP+1
    elif Ti == 2:
        nM = nM+1
        
P = int(input())
M = int(input())

if nP >= P and nM >= M:
    print('S')
else:
    print('N')