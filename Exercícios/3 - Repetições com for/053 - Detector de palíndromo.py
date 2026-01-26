# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. desconsiderando os espaços.

frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(frase)
print('-'*10)
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print(junto)
if inverso == junto:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo")
