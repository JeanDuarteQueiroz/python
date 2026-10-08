lista = set(input("Lista de Laura: ").split(", "))

lista2 = set(input("Lista de Ana: ").split(", "))

ambas = lista & lista2;
um = lista - lista2;
dois = lista2 - lista;
print(f"Itens semelhantes: {", ".join(ambas)} \nItens exclusivos (Laura): {", ".join(um)} \nItens exclusivos (Ana): {", ".join(dois)}");