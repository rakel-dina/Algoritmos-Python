# 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

numero_novo2 = numero_novo1 = operacao = somar = multiplicar = maior = 0
numero_1 = int(input("Digite o 1° número: "))
numero_2 = int(input("Digite o 2° número: "))
print(f"{'MENU':^13.7}\n {'-'*10} \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair no programa\n  ")
operacao = int(input("Qual operação deseja realizar:" ))
while operacao != 5:
    if operacao <=0 or operacao >5:
        print("[INVÁlIDO] Tente novamente.\n")
        print(f"{'MENU':^13.7}\n {'-'*10} \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair no programa\n  ")
        operacao = int(input("Qual operação deseja realizar:" ))
    else:
        if operacao == 1:
            somar = numero_1 + numero_2
            print(f"A soma de [{numero_1}] e [{numero_2}] é {somar}\n")
        if operacao == 2:
            multiplicar = numero_1 * numero_2
            print(f"A multiplicação de [{numero_1}] e [{numero_2}] é {multiplicar}\n")
        if operacao == 3:
            maior = numero_1
            if numero_2 > maior:
                maior = numero_2
            print(f"O maior número entre [{numero_1}] e [{numero_2}] é {maior}")
        if operacao == 4:
            print("Digite os novos números\n")
            numero_novo1 = int(input("Digite o 1° número: "))
            numero_novo2 = int(input("Digite o 2° número: "))
            numero_1 = numero_novo1
            numero_2 = numero_novo2
        operacao = int(input("Qual operação deseja realizar: " ))
        print('-'*20)
print("fim")