#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento

preco1 = float(input('Valor: R$ '))
preco2 = float(input('Valor: R$ '))
preco3 = float(input('Valor: R$ '))
print('Forma de pagamento')
print(10*'-')
print('[1] à vista/ dinheiro\n[2] á vista/ cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão')
preco_total = (preco1 + preco2 + preco3)
opcao = int(input('Qual a forma de pagamento: '))
if opcao == 1:
    print(f'o valor total das compras à vista no dinheiro é: R$ {preco_total:.2f} ')
elif opcao == 2:
    print(f'o valor total das compras à vista no cartão é: R$ {preco_total:.2f} ')
elif opcao == 3:
    print(f'o valor total das compras  é R$ {preco_total:.2f}, em 2X no cartão fica 2 parcelas de: R$ {preco_total/2:.2f}')
else:
    vezes = int(input('Quantas vezes: '))
    juros = ((preco_total/100)*3)
    print(juros)
    print(f'O valor total das compras é R$ {preco_total:.2f}, em {vezes}x no cartão com 3% de juros, fica: {preco_total+juros:.2f} com parcelas de {(preco_total+juros)/3:.2f}')