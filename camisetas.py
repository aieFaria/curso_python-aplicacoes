#!/usr/bin/env python3
#/data/user/0/ru.iiec.pydroid3/files/x86_64-linux-android/bin/python3

N = input()
nP = 0
nM = 0

Ti = input().split()
#Ti = Ti.split()
#print(Ti)
        
P = int(input())
M = int(input())

if P >= Ti.count('1') and M >= Ti.count('2'):
    print('S')
else:
    print('N')