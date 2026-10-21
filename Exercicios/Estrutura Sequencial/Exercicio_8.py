'''
Faça um programa que pergunte
quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

valor = float(input("Digite o valor por hora trabalhada:  "))
horas = float(input("Digite a quantidade de horas trabalhadas:  "))

print(f"O salário esse mês será de {valor*horas}")