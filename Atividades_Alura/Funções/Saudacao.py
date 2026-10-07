def saudacao (horario):
    if horario > 18:
        return "Boa noite"
    elif horario > 12:
        return "Boa tarde"
    else: 
        return"Bom dia"
    
print(f"{saudacao(int(input("Digite o horário:  ")))}")