#!/data/user/0/ru.iiec.pydroid3/files/x86_64-linux-android/bin/python3
from random import randint
import os
from time import sleep

class Mundo:

    def __init__(self, tam=1):
        self.tamanho = tam
        self.data = [[' # ' for _ in range(tam)] for _ in range(tam)]

    def __str__(self):
        string = ''
        for x in self.data:
            for y in x:
                string = string + y
            string = string + '\n'
        return string
    
    def tesouro(self):
        sorteio1 = randint(self.tamanho-self.tamanho,self.tamanho-1)
        sorteio2 = randint(self.tamanho-self.tamanho,self.tamanho-1)
        self.data[sorteio1][sorteio2] = '\033[01;31m X \033[m'
        return [sorteio1, sorteio2]
    
    def cima(self):
        pass
        
    def baixo(self):
        pass
        
    def direita(self):
        pass
        
    def esquerda(self):
        pass

    def tamanhos(self):
        return 


class Jogador(Mundo):
    
    def __init__(self, nome=' '):
        self.nome = f'\033[01;34m '+nome+f' \033[m'

    def __str__(self):
        return f'{self.nome}'

    def iniciar(self, tam):
        self.tamanhos = tam
        a = self.tamanhos
        self.posicaoX = randint(a - a, a-1)
        self.posicaoY = randint(a - a, a-1)
        tabela.data[self.posicaoX][self.posicaoY] = f'{self.nome}'

    def cima(self):
        tabela.data[self.posicaoX][self.posicaoY] = f' . '
        self.posicaoX = self.posicaoX - 1 if self.posicaoX - 1 >= 0 else 0
        tabela.data[self.posicaoX][self.posicaoY] = f'{self.nome}'
        return [self.posicaoX, self.posicaoY]
        
    def direita(self):
        tabela.data[self.posicaoX][self.posicaoY] = f' . '
        self.posicaoY = self.posicaoY + 1 if self.posicaoY + 1 <= self.tamanhos else self.tamanhos
        tabela.data[self.posicaoX][self.posicaoY] = f'{self.nome}'
        return [self.posicaoX, self.posicaoY]
        
    def baixo(self):
        tabela.data[self.posicaoX][self.posicaoY] = f' . '
        self.posicaoX = self.posicaoX + 1 if self.posicaoX + 1 <= self.tamanhos else self.tamanhos
        tabela.data[self.posicaoX][self.posicaoY] = f'{self.nome}'
        return [self.posicaoX, self.posicaoY]
        
    def esquerda(self):
        tabela.data[self.posicaoX][self.posicaoY] = f' . '
        self.posicaoY = self.posicaoY - 1 if self.posicaoY - 1 >= 0 else 0
        tabela.data[self.posicaoX][self.posicaoY] = f'{self.nome}'
        return [self.posicaoX, self.posicaoY]

            
if __name__ == '__main__':
    gab = Jogador(input('\nInsira char: ').upper())

    tabela = Mundo(10)
    
    tesouro = tabela.tesouro()
    gab.iniciar(10)
    print(tabela)

    while True:
        move = input('Ação: ').upper()
        if move == 'W':
            gab.cima()
        elif move == 'A':
            gab.esquerda()
        elif move == 'S':
            gab.baixo()
        elif move == 'D':
            gab.direita()
        else:
            print('Reiniciando jogo')
            sleep(5)
            os.system("./animacao.py")
            break

        os.system("clear")
        print(tabela)
        if gab.posicaoX == tesouro[0] and gab.posicaoY == tesouro[1]:
            print(f'\nPARABÉNS {gab.nome} VOCÊ ENCONTROU O TESOURO')
            break



# Signature ███████████████████████████████████████████████████████████████
# animacao.py : Exercitando POO em exercicio simples
#            
# Github   : 
# data     : 25/01/2024
# autor    : Gabriel Faria,
#            Engenheiro da Computação em formação
# linguagem: Python 3.11.4 on Linux
# █████████████████████████████████████████████████████████████████████████