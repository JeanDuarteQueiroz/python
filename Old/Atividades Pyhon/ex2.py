#2. Conversor de temperatura

#Escreva um programa em Python para converter temperaturas entre Celsius e Fahrenheit.

#[Fórmula: c/5 = f-32/9 [onde c = temperatura em Celsius e f = temperatura em Fahrenheit]

#Resultado esperado :

#60°C equivale a 140 graus Fahrenheit.
#45°F equivale a 7 graus Celsius.

x=0;

def converteParaFahrenheit (tempCelsius):
    tempFahrenheit = ((tempCelsius * 9) / 5) + 32;
    return tempFahrenheit

def converteParaCelsius (tempFahrenheit):
    tempCelsius = ((tempFahrenheit - 32) * 5) / 9
    return tempCelsius

while x != 3:
    x = int(input( 
    """ 
    Escolha uma das opções: 
    
    1 - Converter Celsius para Fahrenheit

    2 - Converter Fahrenheit para Celsius

    3 - Finalizar programa; 

    """));

    if x == 1:
        temp = int(input("Informe a temperatura em Celsius:  "));
        print(f"\nA temperatura em Celsius convertida em Fahrenheit é: {converteParaFahrenheit(temp)}");
    elif x == 2:
        temp = int(input("Informe a temperatura em Fahrenheit:  "));
        print(f"\nA temperatura em Fahrenheit convertida em Celsius é: {converteParaCelsius(temp)}");
    elif x == 3:
        print("Finalizando programa...");
    else:
        print("Informe uma opção válida.");