#!/data/user/0/ru.iiec.pydroid3/files/x86_64-linux-android/bin/python3

N = int(input())
numeros = []
tamanho = 0

for i in range(N):
    numero = int(input())
    if numero != 0:
        numeros.append(numero)
        tamanho = tamanho + 1
    else:
        del(numeros[tamanho-1])
        tamanho = tamanho - 1
    #print(numeros)

print(sum(numeros))