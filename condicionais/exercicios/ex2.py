#A loja virtual FIAP Wear, que vende roupas personalizadas da instituição, disponibilizou no mês do aniversário o cupom NIVER10, que concede 10% de desconto no valor total de uma compra feita no site.
# Caso o cliente digite o cupom corretamente, deverá ser infomrado do valor final da compra já com o desconto aplicado. Caso digite o cupom de forma incorreta, deverá ser informado do valor da compra sem o desconto.
# Esse problema claramente pede o uso de um if composto!! Afinal de contas, temos uma única condição (o Cupom digitado ser igual a "NIVER10") e das duas condições, sendo uma para cada resultado da condição.

valor_compra = input("Informe o valor total da compra:  ");
cupom = input("Informe o cupom de desconto:  ").upper();

valor_compra = float(valor_compra);

if (cupom) == "NIVER10":
    valor_compra -= valor_compra * 0.10
    print("Valor total da sua compra ficou: {}".format(valor_compra));
else:
    print("Cupom Inválido!")
    print("Valor total da sua compra ficou: {}".format(valor_compra));