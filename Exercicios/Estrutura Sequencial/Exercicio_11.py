'''
Exercício 11
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

O produto do dobro do primeiro com metade do segundo .
A soma do triplo do primeiro com o terceiro.
O terceiro elevado ao cubo.
'''

num1 = int(input("Digite um número inteiro:  "))
num2 = int(input("Digite outro número inteiro:  "))
num3 = float(input("Digite um número real:  "))

print(f"O produto do dobro do primeiro com a metade do segundo é: {(num1 * 2) * (num2/2)}\n A soma do triplo do primeiro com o terceiro é {(num1 * 3) + num3}\n O terceiro elevado ao cubo é {num3**3}")