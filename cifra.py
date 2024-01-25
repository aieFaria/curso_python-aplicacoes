#!/data/user/0/ru.iiec.pydroid3/files/x86_64-linux-android/bin/python3


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']
texto = input().lower()


def algVogal(constante):
    vogal = ' '

    posicaoVogais = [alfabeto.index(v) for v in vogais]
    menor = 99
    for i in range(len(posicaoVogais)):
        c = alfabeto.index(constante)
        d = posicaoVogais[i]
        sub = c - d if c > d else d - c
        if sub < menor:
            menor = sub
            posicaoMenor = i
    return vogais[posicaoMenor]


final = ''
for i in texto:
    composicao = ''
    if vogais.count(i)!=0:
        final = final + f'{i}'
    else:
        for x in range(3):
            p = alfabeto.index(i if i!='z' else 'x', 0, 24)

            if x == 0:
                composicao = f'{i}'
            elif x == 1:
                composicao = composicao + algVogal(i)
            else:
                composicao = composicao + alfabeto[p+1] if vogais.count(alfabeto[p+1]) == 0 else composicao + alfabeto[p+2]  
        final = final + composicao
print(final)





# Signature ███████████████████████████████████████████████████████████████
# cifra.py : Olimpíada Brasileira de Informática – OBI2021 – Prog. Nível 2 – Fase 1
#            Uma solução para o problema 'Cifra da Nlogônia'
# Github   : 
# data     : 25/01/2024
# autor    : Gabriel Faria,
#            Engenheiro da Computação em formação
# linguagem: Python 3.11.4 on Linux
# █████████████████████████████████████████████████████████████████████████