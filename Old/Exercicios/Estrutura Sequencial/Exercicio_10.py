'''
Faça um programa que peça a temperatura
em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

temp = float(input("Digite a temperatura em Celsius: "))
print(f"A temperatura convertida em F° é {(temp * (9/5) + 32):.1f}")