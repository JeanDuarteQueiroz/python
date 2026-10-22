'''
Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.

Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

Exemplo de Entrada:
'''

lista = []
while True:
    item = input("Digite o nome do integrante ou 'sair':  ").title()
    if item == "Sair":
        break
    else:
        lista.append(item)
        continue
print(f"Voluntários registrados: {lista}")