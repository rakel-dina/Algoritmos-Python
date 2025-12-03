# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu índice de
#massa corporal (IMC) e mostre seus status, de acordo com a tabela abaixo:
# - abaixo de 18,5: abaixo do peso
# - entre 18,5 e 25: Peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - acima de 40: obesidade mórbida
peso = float(input('Seu peso: '))
altura = float(input('Sua altura: '))
imc = peso/(altura**2)
if imc <18.5:
    print('Abaixo do peso | IMC:', end=' ')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal | IMC:', end=" ")
elif imc >=25 and imc <30:
    print("Sobrepeso | IMC:", end=" ")
elif imc >= 30 and imc <40:
    print('Obesidade | IMC:', end=" ")
else:
    print('Obesidade Mórbida | IMC:', end=" ")
print(f"{imc:.1f}")