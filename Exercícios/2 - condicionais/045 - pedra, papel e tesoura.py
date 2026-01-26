from random import randint
from time import sleep
print('[0]PEDRA\n[1]PAPEL\n[2]TESOURA')
print(20*'/')
computador = (randint(0,2))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print(f'Você jogou: {itens[jogador]}')
print(f'O computador jogou: {itens[computador]}')
if computador == 0: # pedra
    if jogador == 0: # pedra
        print('EMPATE')
    elif jogador == 1: # papel
        print("JOGADOR GANHA")
    elif jogador ==2: # tesoura
        print("COMPUTADOR GANHA")
elif computador == 1: # papel
    if jogador == 0:  # pedra
        print('COMPUTADOR GANHA')
    elif jogador == 1:  # papel
        print("EMPATE")
    elif jogador == 2:  # tesoura
        print('JOGADOR GANHA')
elif computador == 2: # tesoura
    if jogador == 0:  # pedra
        print('JOGADOR GANHA')
    elif jogador == 1:  # papel
        print("COMPUTADOR GANHA")
    elif jogador == 2:  # tesoura
        print('EMPATE')
