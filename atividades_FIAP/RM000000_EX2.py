valor_carro = float(input("Digite o preço do carro:  "));

qnt_parcela = 1;
juros = 0;

for x in range(0,11,1):
    if qnt_parcela == 1:
        print("O preço à vista do carro com desconto de 20% é: {:.1f}".format(valor_carro-(valor_carro*0.2)));
        qnt_parcela += 5;
        juros += 3;
    else:
        valor_juros = valor_carro + (valor_carro*(juros/100));
        print("O preço final parcelado em {} X é de R$ {:.2f} com parcelas de {:.2f}".format(qnt_parcela, valor_juros, valor_juros/qnt_parcela));
        qnt_parcela += 6
        juros += 3;

