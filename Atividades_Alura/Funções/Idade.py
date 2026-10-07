def idade (ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento

nascimento = int((input("Digite o ano de seu nascimento:  ")))
atual = int((input("Digite o ano atual:  ")))

print(f"Minha idade é: {idade(atual, nascimento)}");20