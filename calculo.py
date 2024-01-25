#!/data/user/0/ru.iiec.pydroid3/files/x86_64-linux-android/bin/python3

dados = dict(zip(['S', 'A', 'B'], [int(input()) for i in range(3)]))

contagem = 0
for i in range(dados['A'], dados['B']+1):
    digitos = [int(x) for x in f'{i}']

    if sum(digitos) == dados['S']:
        contagem = contagem + 1
        
print(contagem)