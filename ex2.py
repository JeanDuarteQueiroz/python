'''
Praticando um pouco Dict Comprehetion
'''

produtos = {
    'Café': {"Quantidade": 5, "Preço": 12},
    'Feijão': {"Quantidade": 5, "Preço": 10},
    'Cerveja':{"Quantidade": 19, "Preço": 6}
}

produto_desconto = {
    nome: {
        "Quantidade": dados["Quantidade"],
        "Preço": dados["Preço"] * 0.9 if dados["Preço"] < 15 else dados["Preço"]
    }
    for nome, dados in produtos.items()
}

print(produto_desconto)