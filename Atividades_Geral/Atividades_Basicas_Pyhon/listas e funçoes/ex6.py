#Exercício 6: Integração (Funções + Listas)
#Escreva uma função chamada filtrar_maiores(lista, limite) que recebe uma lista de números e um valor limite. 
# A função deve retornar uma nova lista 
# contendo apenas os elementos que forem estritamente maiores do que o limite informado.

lista = [10, 25, 3, 40, 15];
resultado = [];
# resultado = filtrar_maiores([10, 25, 3, 40, 15], 18)

def filtrarMaiores (lista, lim):
    listaMaior = [];
    for x in range (0,len(lista),1):
        if lista[x] > lim:
            listaMaior.append(lista[x]);
    return listaMaior;

# Deve retornar: [25, 40]

resultado = filtrarMaiores(lista, 8);
print(f"A nova lista fica: {resultado}");