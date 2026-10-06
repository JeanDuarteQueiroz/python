#1. Divisível por 7 e múltiplos de 5

#Escreva um programa em Python para encontrar os números que são divisíveis por 7 e múltiplos de 5, entre 1500 e 2700 (inclusive).

n1 = []

for x in range (1500,2701,1):
    if x % 7 == 0 and x % 5 == 0:
        n1.append(str(x));
    else:
        continue
print(", ".join(n1));