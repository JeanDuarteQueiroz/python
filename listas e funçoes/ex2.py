# Dada a seguinte lista:

numeros = [12, 5, 8, 21, 30, 7, 14, 3, 18];

# Escreva um programa que percorra essa lista e crie duas novas listas:

listaImpar = [];
listaPar = [];

# Uma lista apenas com números pares.
def pegaPareImpar (lista):
    listaPar = [];
    listaImpar = [];
    for x in range(0,len(numeros),1):
        if numeros[x] % 2 == 0:
            listaPar.append(numeros[x]);
        else:
            listaImpar.append(numeros[x]);
    return listaPar, listaImpar;

listaPar, listaImpar = pegaPareImpar(numeros);

print(f"Essa é a lista dos pares:\n {listaPar}")
print(f"Essa é a lista dos impares:\n {listaImpar}")