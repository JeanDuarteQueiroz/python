
# Verificação de Finobacci (1,1,2,3,5,8,13,21...)

numero = int(input("Digite um número:  "));

x, y = 0, 1;

while x < numero:
    x, y = y, x + y;

if x == numero:
        print("Acertou!");
else:
        print("Errou!");
