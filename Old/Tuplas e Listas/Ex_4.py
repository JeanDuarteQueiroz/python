'''
Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?

Exemplo de Entrada:
'''
estoque1 = ("Arroz", "Feijão", "Macarrão")
estoque2 =  ("Óleo", "Sal", "Açúcar")
estoque = estoque1 + estoque2
print(f"Estoque unificado: \n{estoque}")