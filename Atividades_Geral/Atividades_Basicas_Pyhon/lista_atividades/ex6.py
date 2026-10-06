#Calcule o cubo de todos os números de 1 até um número dado.
import math # Muito mais fácil usando as funções prontas...
num = int(input("Digite um número:  "));
#cubo = 0; 
for x in range(1,num+1,1):
    #cubo = x * x * x;
    print(f" O cubo de {x} é {pow(x,3)}");