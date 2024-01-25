#!/data/user/0/ru.iiec.pydroid3/files/x86_64-linux-android/bin/python3
grupo = -1
con = [input() for i in range(6)]

if con.count('V') >= 5:
    grupo = 1
if 4 >= con.count('V') > 2:
    grupo = 2
if 2 >= con.count('V') >=1:
    grupo = 3

print(grupo)