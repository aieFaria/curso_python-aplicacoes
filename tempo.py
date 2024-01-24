#!/data/user/0/ru.iiec.pydroid3/files/x86_64-linux-android/bin/python3
#/usr/bin/env python3

N = int(input())
tempo = 1;
ok = 0;
ultima = [None for i in range(100)]
pendenteLogico = [None for i in range(100)]
saldoTempo = [0 for i in range(100)]


for i in range(N):
    dados = list(input().split())
    c = dados[0].upper()
    n = int(dados[1])

    if c == 'T':
        tempo = n + tempo
        ok = 0;
    elif c == 'R':
        tempo = ok + tempo
        ok = 1
        ultima[n] = tempo
        pendenteLogico[n] = True
    else:
        tempo = ok + tempo
        ok = 1
        saldoTempo[n] = (tempo - ultima[n]) + saldoTempo[n]
        pendenteLogico[n] = False

for i in range(100):
    if ultima[i]:
        print(f'{i} ', end='')
        print('-1') if pendenteLogico[i] else print(saldoTempo[i])
