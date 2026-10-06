valor_bruto = int(input("Informe o valor bruto do pacote:  "));
categoria = input("Informe a categoria (Eco, Exe, Pri) dos assentos:  ").upper();
viajantes = int(input("Informe a quantidade de viajantes:  "));

if (categoria) == "ECO":
    print("Verificando numero de viajantes... ");
    if (viajantes) <= 2:
        desconto = 0.03;
    elif (viajantes) == 3:
        desconto = 0.04;
    else:
        desconto = 0.05;
    valor_liquido = valor_bruto - (valor_bruto * desconto);
    print("O valor total do pacote é: {}".format(valor_bruto))
    print("O valor do desconto é: {}".format(valor_bruto * desconto))
    print("O valor liquido será: {}".format(valor_liquido));
    print("O valor médio (arredondado) por viajante é: {:.2f}".format(valor_liquido/viajantes));
elif (categoria) == "EXE":
    print("Verificando numero de viajantes... ");
    if (viajantes) <= 2:
            desconto = 0.05;
    elif (viajantes) == 3:
        desconto = 0.07;
    else:
        desconto = 0.08;
        valor_liquido = valor_bruto - (valor_bruto * desconto);
        print("O valor total do pacote é: {}".format(valor_bruto))
        print("O valor do desconto é: {}".format(valor_bruto * desconto))
        print("O valor liquido será: {}".format(valor_liquido));
        print("O valor médio (arredondado) por viajante é: {:.2f}".format(valor_liquido/viajantes));
elif (categoria) == "PRI":
    print("Verificando numero de viajantes... ");
    if (viajantes) <= 2:
        desconto = 0.1;
    elif (viajantes) == 3:
        desconto = 0.15;
    else:
        desconto = 0.2;
    valor_liquido = valor_bruto - (valor_bruto * desconto);
    print("O valor total do pacote é: {}".format(valor_bruto))
    print("O valor do desconto é: {}".format(valor_bruto * desconto))
    print("O valor liquido será: {}".format(valor_liquido));
    print("O valor médio (arredondado) por viajante é: {:.2f}".format(valor_liquido/viajantes));
else:
    print("Nenhuma categoria válida foi informada!");