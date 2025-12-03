#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
#mostre os 10 primeiros termos dessa progressão.
print('Primeiros 10 termos de uma PA')
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Qual a razão: '))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c} -', end=" ")




