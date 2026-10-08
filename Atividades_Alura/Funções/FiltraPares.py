numeros = input("Digite numeros separados por espeço:  ").split()
pares = filter(lambda x: int(x) % 2 == 0, numeros)
print("Esses são os números pares:  ", " ".join(pares))