#!/data/user/0/ru.iiec.pydroid3/files/x86_64-linux-android/bin/python3
from random import randint

caracteres=['.', '█', '░']

print('\033[01;35m')
for i in range(10):
    
    print(''.join(caracteres[randint(0, 1)] for i in range(76)))
print('\033[m')
