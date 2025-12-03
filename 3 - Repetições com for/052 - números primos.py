#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
tot = 0
print('==IDENTIFICANDO NÚMEROS PRIMOS==')
num = int(input('Digite um número: '))
for c in range (1, num +1, 1):
    if num % c == 0:
        print('\033[33m', end=" ")
        tot = tot +1
    else:
        print('\033[31m', end=" ")
    print(c, end=" ")

print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print(f'Por isso {num} é um número primo.')
else:
    print(f'Por isso {num} não é um número primo.')