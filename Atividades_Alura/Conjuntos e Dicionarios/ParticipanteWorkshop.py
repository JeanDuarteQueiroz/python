
participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

}

participante = input("Informe o nome do participante a ser removido: ");
    
print("Lista atualizada de participantes:")
for chave, valor in participantes.items():
    valor.discard(participante);
    print(f"{chave}: {valor}");