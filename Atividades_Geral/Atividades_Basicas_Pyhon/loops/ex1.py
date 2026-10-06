quantidade_alimentos = int(input("Informe a quantidade de alimentos consumidos hoje:  "));
x = 0
caloria_total = 0;

for x in range(1,quantidade_alimentos,1):
    alimento = input("Informe o nome do alimento:  ");
    calorias_alimento = float(input(f"Informe a quantidade de calorias(Kcal) de {alimento}:  "));
    caloria_total = caloria_total + calorias_alimento;
print("O total de calorias ingerido foi: {}".format(caloria_total));