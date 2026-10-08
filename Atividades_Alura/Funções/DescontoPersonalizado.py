def cria_desconto (p):
    def valor_desconto (valor):
        return valor - ( valor * (p/100));
    return valor_desconto

desc = float(input("Informe a porcentagem de desconto:  "));
p_desconto = cria_desconto(desc);

valor = float(input("Informe o valor total:  "));
print(f"O valor final fica: {p_desconto(valor)}")
