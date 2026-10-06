# Dada a seguinte lista:

numeros = [12, 5, 8, 21, 30, 7, 14, 3, 18];

# Escreva um programa que percorra essa lista e crie duas novas listas:

listaImpar = [];
listaPar = [];

# Uma lista apenas com números pares.

for x in numeros:
    if x % 2 == 0:
        listaPar.append(x);
    else:
        listaImpar.append(x);

print(f"Essa é a lista dos pares:\n {listaPar}")
print(f"Essa é a lista dos impares:\n {listaImpar}")