valor = input("Informe a temperatura (ex> 60c, 140f):  ");

# retirar a parte númerica.
temp = int(valor[:-1]);

# retira a instrução.
i = str(valor[-1].upper());

if i == "C":
    fahrenheit = ((temp * 9) / 5) + 32;
    print(f"A temperatura convertida para Fahrenheit é {fahrenheit}")
elif i == "F":
    celsius = ((temp - 32) * 5) / 9;
    print(f"A temperatura convertida para Celsius é {celsius}")
else:
    print("Temperatura inválda! Informe 'C' para Celsius ou 'F' para Fahrenheit.");