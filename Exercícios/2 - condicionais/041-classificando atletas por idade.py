##A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER
import datetime
from datetime import date
nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nascimento
print(f'O atleta tem {idade} anos de idade.')
if idade <= 9 :
    print('Atleta: MIRIM')
elif idade <=14:
    print('Atleta: INFANTIL')
elif idade <= 19:
    print('Atleta: JUNIOR')
elif idade <=25:
    print('Atleta: SÊNIOR')
else:
    print('Atleta: MASTER')