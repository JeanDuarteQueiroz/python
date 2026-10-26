'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
from math import ceil

tamanho = float(input("Digite o tamanho em M2 a ser pintado:  "))
litros_necessarios = tamanho / 6
litros_necessarios_bonus= ((tamanho*0.1)+tamanho) / 6
print(f"Comprando apenas em galões de 18 litros: {ceil(litros_necessarios/18)} Litros = R$ {ceil(litros_necessarios/18)*80}")
print(f"Comprando apenas em galões de 3,6 litros: {ceil(litros_necessarios/3.6)} Litros = R$ {ceil(litros_necessarios/3.6)*25}")


if litros_necessarios_bonus < 10.8:
    print(f"Comprando misturado: Galões de 18 litros: 0, custando R$ 0,00 e Galões de 3,6 litros: {ceil(litros_necessarios_bonus/3.6)} custando R$ {ceil(litros_necessarios_bonus/3.6) * 25}")
elif litros_necessarios_bonus < 18:
    print(f"Comprando misturado: Galões de 18 litros: {ceil(litros_necessarios_bonus/18)} custando R$ {ceil(litros_necessarios_bonus/18)*80}, e Galões de 3,6 litros: 0 custando R$ 0,00")
else:
    total_18 = round(litros_necessarios_bonus / 18)
    total_livre = litros_necessarios_bonus - (total_18 * 18) 
    print(f"Comprando misturado: : {total_18} Galões de 18 litros custando R$ {total_18 * 80}, e {ceil(total_livre/3.6)} Galões de 3,6 litros custando R$ {ceil(total_livre/3.6)*25}")    