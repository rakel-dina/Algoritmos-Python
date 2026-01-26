#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
print(f'A soma dos {cont} números pares digitados é {s}')
