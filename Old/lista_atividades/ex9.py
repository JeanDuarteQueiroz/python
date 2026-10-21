#Imprima os elementos de uma lista presentes em posições de índice ímpares.

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def pegaIndiceImpar (lista):
    listaImpar = [];
    for x in range (0,len(lista),1):
        if x % 2 == 0:
            continue
        else:
            listaImpar.append(lista[x]);
    return listaImpar

listaNova = pegaIndiceImpar(lista);
print(f"Essa é a lista dos índices ímpares: \n {listaNova}");