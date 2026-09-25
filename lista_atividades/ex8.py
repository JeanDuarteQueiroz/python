#Conte as ocorrências de um elemento específico em uma lista

lista = [10, 20, 10, 30, 10, 40, 50];

def contaLista (lista, num):
    vezes = 0;
    for x in lista:
        if x == num:
            vezes += 1;
        else:
            continue
    return vezes

numeroVezes = contaLista(lista,10)
print(f"O número 10 apareceu {numeroVezes} vezes.")