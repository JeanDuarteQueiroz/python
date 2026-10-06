#Escreva uma função chamada eh_par(numero) que recebe um número inteiro como parâmetro 
# e retorna True se o número for par e False caso contrário. 
# Teste a função com os valores 7 e 12.

def paridade (num):
    if num % 2 == 0:
        return True
    return False

print(f"{paridade(12)}");
print(f"{paridade(7)}");