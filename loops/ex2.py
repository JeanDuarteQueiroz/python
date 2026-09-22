quantidade = int(input("Informe o total de transações realizadas:  "));
valor_total = 0;

for x in range(1,quantidade,1):
    motivo = input(f"Informe o motivo da transação {x}:  ");
    valor = float(input(f"Informe o valor da transação {motivo}:  "));
    valor_total = valor_total + valor;
print(f"O valor total das transações foi {valor_total}");
print(f"O valor médio das transações foi {valor_total/quantidade}");