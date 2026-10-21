'''
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
'''
valor_hora = float(input("Digite o valor ganho por hora:  "))
horas = float(input("Digite a quantidade de horas trabalhadas no mês:  "))
bruto = valor_hora * horas
inss = bruto * (11/100)
irpf = bruto * (8/100)
sindicato = bruto * (5/100)

print(f"+ Salário Bruto: R$ {bruto:.1f}\n- INSS (11%): R$ {inss:.1f}\n- IRPF (8%): R$ {irpf:.1f}\n- Sindicato (5%): R$ {sindicato:.1f}\n= Salário Líquido: R$ {bruto - irpf - inss - sindicato:.1f}")