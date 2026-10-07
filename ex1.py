'''
Praticando com listas e lista comprehention.
'''

produtos = [
    ('Feijão', 6.99, 20),
    ('Arroz', 5.99, 5),
    ('Refrigerante', 7.99, 25),
    ('Lasanha', 12.99, 1),
    ('Cerveja', 4.99, 19),
]

precos = sum([produto[1] for produto in produtos]);

#for x in produtos:
#   precos.append(x[1]);    
    
print(precos);


status_estoque = [
    [produto[0], 'Estoque abaixo do mínimo' if produto[2] < 20 else 'Estoque ok']
     for produto in produtos
]

print(status_estoque);