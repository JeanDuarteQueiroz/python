
tipo_inv = 0;
aliquota = 0;

while True: #Laço que valida o investimento informado. 
    
    tipo_inv = int(input("Escolha o tipo de investimento:  \n 1. CDB\n 2. LCI \n 3. LCA\nDigite o tipo de investimento(1,2 ou 3):  "));
    
    if tipo_inv == 1:
        
        valor_resgate = int(input("Digite o valor a ser resgatado:  "));
        dias_resgate = int(input("Digite o número de dias que o valor permaneceu investido:  "));
        
        if dias_resgate <= 180:
            aliquota = 22.5 / 100; 
            print("O valor do imposto de renda a ser pago é: R${:.2f}".format(valor_resgate * aliquota));
            break
        elif dias_resgate > 180 and dias_resgate <= 360:
            aliquota = 20 / 100;
            print("O valor do imposto de renda a ser pago é: R${:.2f}".format(valor_resgate * aliquota));
            break
        elif dias_resgate > 360 and dias_resgate <=720:
            aliquota = 17.5 / 100;
            print("O valor do imposto de renda a ser pago é: R${:.2f}".format(valor_resgate * aliquota));
            break
        else:
            aliquota = 15 / 100;
            print("O valor do imposto de renda a ser pago é: R${:.2f}".format(valor_resgate * aliquota));
            break
        
    elif tipo_inv == 2 or tipo_inv == 3:
        valor_resgate = int(input("Digite o valor a ser resgatado:  "));
        dias_resgate = int(input("Digite o número de dias que o valor permaneceu investido:  "));
        print("O valor do imposto de renda a ser pago é: R${:.2f}. Para esse tipo de Investimento o IR é Isento".format(valor_resgate * aliquota));
        break 
    else:
        print("\n Opção Inválida - Escolha uma opção válida de Investimento!!\n");

    