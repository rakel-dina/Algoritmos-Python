# 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

operacao = 0
numero_1 = int(input("Digite o 1° número: "))
numero_2 = int(input("Digite o 2° número: "))
print(''*10)
while operacao != 5:
    print(f"{'MENU':^13.7}\n {'-' * 10} \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair no programa\n  ")
    operacao = int(input("Qual operação deseja realizar:"))
    if operacao == 1:
        somar = numero_1 + numero_2
        print(f"SOMA | [{numero_1}] + [{numero_2}]: {somar}\n")
    elif operacao == 2:
        multiplicar = numero_1 * numero_2
        print(f"MULTIPLICAÇÃO | [{numero_1}] x [{numero_2}]: {multiplicar}\n")
    elif operacao == 3:
        if numero_1 > numero_2:
            maior = numero_1
        else:
            maior = numero_2
        print(f"MAIOR NÚMERO | ENTRE [{numero_1}] E [{numero_2}],  [{maior}] É MAIOR\n")
    elif operacao == 4:
        print("Digite os novos números\n")
        numero_1 = int(input("Digite o 1° número: "))
        numero_2 = int(input("Digite o 2° número: "))

       # operacao = int(input("Qual operação deseja realizar: " ))
    elif operacao == 5:
        print("FINALIZANDO\n")
       #print('-'*20)
    else:
        print("[OPÇÃO INVÁLIDA], tente novamente.\n")
print("fim")