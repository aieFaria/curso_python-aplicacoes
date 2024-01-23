#!/data/user/0/ru.iiec.pydroid3/files/aarch64-linux-android/bin/python3
from random import randint

# Separação cores
cores = ['\033[m', '\033[01;31m', '\033[01;32m']


# Func gera num aleatorio
def geraAleatorio(dif=0, intervalo=(1, 60)):
    all = dif
    while True:
        if all != dif:
            return all
        else:
            all = randint(*intervalo)

# Func gera jogos, em dicionario
def geraJogo(qntd, intervalo=(1, 60), numJogos=1):
     jogo={}
     for j in range(numJogos):
         num = []
         aleatorio = randint(*intervalo)
         
         #List comprehension
         num = [aleatorio if num.count(aleatorio)>=1 else geraAleatorio(dif=aleatorio, intervalo=intervalo) for i in range(qntd)]
         jogo[f'Jogo {j+1}'] = num
     
     return jogo
            
            
# Verifica se está no módulo main                 
if __name__ == '__main__':
    gerados = geraJogo(6, numJogos=100, intervalo=(1, 60))
    teste = [1, 32, 60, 55, 18, 13]
    
    for jogo in gerados.items():
        comp = list(set(teste).intersection(jogo[1]))
        
        i = 2 if len(teste) == len(jogo[1]) and len(comp) == len(teste) else 1
        
        print(f'{cores[i]}{jogo[0]}: {jogo[1]}{cores[0]}')
        if i == 2:
          print('Houve ganhador!!!')
          break
          