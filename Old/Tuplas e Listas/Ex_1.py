'''
Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.

Exemplo de Entrada:
'''
despensa = ["arroz", "feijao", "açucar"]

item = input("Digite um item: ").lower().strip();
if item not in despensa:
    print(f"{item} não está na Despensa, é necessário comprar")
else:
    print(f"{item} está na Despensa, não é necessário comprar.")