'''
Função que recebe a lista quebrada e em Str ex: ["1","2","3","","4","5"] e converte ela uma lista em blocos inteiros do topo int ex: [123,45]

def converteListaToInt (lista):
    nova_lista = []
    tmp = ""
    for x in lista:
        if x == " ":
            if tmp:
                nova_lista.append(tmp)
                tmp ="";
        else:
            tmp += x
    if tmp:
        nova_lista.append(tmp);
    return [int(item) for item in nova_lista]

soma = somaLista(input("Digite seus valores ex:(10 20 50):  "))
print(f"A soma dos seus valores é:  {sum(soma)}");
'''

lista = input("Digite seus valores: ").split(" ")
print(sum(map(float, lista)));

