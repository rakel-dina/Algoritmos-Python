# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
cont = 0
soma_idade = 0
nome_h_velho = 0
maior_h_velho = 0
mulher20 = 0
for pessoa in range(1,5):
    nome = input(f'Digite o nome da {pessoa}ª pessoa: ').title()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [F] [M]: ').upper().strip()
    print('-'*30)
    cont = cont + 1
    soma_idade = soma_idade + idade
    media = soma_idade / cont
    if pessoa == 1 and sexo == 'M':
        maior_h_velho = idade
        nome_h_velho = nome
    if sexo in 'M' and idade > maior_h_velho:
        maior_h_velho = idade
        nome_h_velho = nome
    if sexo in 'F' and idade <20:
        mulher20 = mulher20 + 1
print('')
print('-'*30)
print(f'A média de idade do grupo é de {media} anos de idade.')
print(f'O nome do homem mais velho é {nome_h_velho} com {maior_h_velho} anos de idade.')
print(f'No grupo tem {mulher20} mulher(s) com menos de 20 anos de idade.')
print('-'*30)