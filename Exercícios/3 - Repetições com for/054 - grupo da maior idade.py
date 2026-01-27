# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
from datetime import datetime
menor = 0
maior = 0
anoatual = datetime.now().year
for c in range(0,7):
    ano_pessoa = int(input('Em qual ano você nasceu: '))
    ano_pessoa = anoatual - ano_pessoa
    if ano_pessoa >= 18:
        maior = maior +1
    else:
        menor = menor + 1
print(f"{menor} pessoas ainda não atingiram a maior idade.")
print(f"{maior} pessoas já são maiores de idade.")




