convidado = set()
x = ""
while True:
    x = input("Digite o nome do convidado (ou Sair):  ").lower();
    if x != "sair":
        convidado.add(x)    
    else: 
        break
print(f"Convidados confirmados: ", ", ".join(convidado));