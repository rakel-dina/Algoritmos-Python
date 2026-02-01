# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que
# agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer.

computador = randint(0,10)
#print(computador)
palpites = 0
print('[ADIVINHE UM NÚMERO DE 0 A 10 QUE O COMPUTADOR PENSOU]')
jogador = int(input('Digite: '))
while jogador != computador:
    print("ERRADO, Tente Novamente: ")
    jogador = int(input('Digite: '))
    palpites = palpites + 1
    if jogador == computador:
        print(f'PARABÉNS! Voce acertou com {palpites} palpites.!')
print("Fim")