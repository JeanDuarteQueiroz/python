participantes = { 

    "Mariana": 25, 

    "Carlos": 32, 

    "Beatriz": 28, 

    "Rafael": 35 

}

print(f"Nomes dos participantes: {", ".join(set(participantes.keys()))}");
print(f"Idade dos participantes: {" ".join(str(x) for x in participantes.values())}");

for nome, idade in participantes.items():
    print(f" -{nome}: {idade} anos");