'''
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

Exemplo de Entrada:
Digite o nome incorreto: Carlos
Digite o nome correto: João
'''

lista = ["Jean", "Jorge", "Carlos"]

invalido = input("Digite o nome incorreto: ")
correto = input("Digite o nome correto: ")

if invalido in lista:
    indice = lista.index(invalido)
    lista.pop(indice)
    lista.insert(indice, correto)
    print(f"{invalido} foi substituido por {correto}")
    print(lista)
else:
    print("Nome não encontrado na lista!")
