valor_divida = int(input("Digite o valor da dívida:  "));

qnt_parcela = 1;
juros = 0;

for x in range (1,6,1):
    if qnt_parcela == 1:
        print("Valor Total: {:.2f}, Juros: {:.2f}, Número de Parcelas: {:.2f}, Valor das Parcelas: {:.2f}".format(valor_divida, juros, qnt_parcela, valor_divida/qnt_parcela))
        qnt_parcela += 2;
        juros += 10;
    else:
        valor_juros = valor_divida*(juros/100);
        print("Valor Total: {:.2f}, Juros: {:.2f}, Número de Parcelas: {:.2f}, Valor das Parcelas: {:.2f}".format(valor_divida+valor_juros, valor_juros, qnt_parcela, (valor_divida+valor_juros)/qnt_parcela))
        qnt_parcela += 3;
        juros += 5;
