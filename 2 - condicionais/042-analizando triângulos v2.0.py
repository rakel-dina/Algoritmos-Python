#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
# triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes
r1 = float(input('primeira reta:'))
r2 = float(input('segunda reta: '))
r3 = float(input('terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar triangulo',end=" ")
    if r1 == r2 == r3:
        print('esquilátero!')
    elif r1 != r2 != r3 != r1:
        print('Isósceles!')
    else:
        print("Escaleno!")
else:
    print('Não pode formar triângulo.')