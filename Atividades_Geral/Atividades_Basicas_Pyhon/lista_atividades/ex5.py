#Escreva a tabuada de multiplicação de um número dado.

num = int(input("Deseja ver a taboada de qual número:  "));
for x in range(1,11,1):
    print(f" {num} X {x} = {num*x} ");
else:
    print(" Pronto!");