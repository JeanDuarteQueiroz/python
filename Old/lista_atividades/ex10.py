# Imprima a lista em ordem inversa usando um loop.

lista = [10, 20, 30, 40, 50];

def listaInversa (litsa):
    resultado = [];
    for x in lista:
        resultado.insert(0,x);
    return resultado

listaNova = listaInversa(lista);
print(f"A lista invertida é: \n {listaNova}");