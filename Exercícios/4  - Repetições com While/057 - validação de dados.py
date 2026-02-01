# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.

sexo = str(input("Qual é o sexo? [F] [M]: ")).strip().upper()
while sexo not in 'FM':
    print(f'INVÁLIDO. Digite apenas [F] ou [M].')
    sexo = str(input("Qual é o sexo? [F] [M]: ")).strip().upper()
print(f'Sexo [{sexo}] registrado com sucesso.')