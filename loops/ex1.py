quantidade_alimentos = int(input("Informe a quantidade de alimentos consumidos hoje:  "));
x = 0
caloria_total = 0;

while x != quantidade_alimentos:
    x = x+1;
    alimento = input("Informe o nome do alimento:  ");
    calorias_alimento = float(input("Informe a quantidade de calorias de {}:  ".format(alimento)));
    caloria_total = caloria_total + calorias_alimento;
print(" O total de calorias ingerido foi: {}".format(caloria_total));