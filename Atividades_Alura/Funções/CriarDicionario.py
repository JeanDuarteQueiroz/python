chaves = input("Digite suas frutas separadas por virgula:  ").split(", ");
valores = input("Digite o valor das frutas separadas por virgula:  ").split(", ");

for chaves, valores in zip(chaves, valores):
    print(f" {chaves.strip()}: {valores.strip()}");

"""
def criaDicionario (chave, valor):
    dicionario = {}
    for chave in chaves:
        for valor in valores:
            dicionario[chave] = valor;
    return dicionario

dicionario = criaDicionario(chaves, valores);
print(dicionario)
"""