#Exercício 4. Calcule a soma de todos os números de 1 a N.

num = int(input("Digite um número:  "));
soma = 0;
for x in range(0,num+1,1):
    soma = soma + x;
else:
    print(f"A soma de todos os números de 1 a {num} é {soma}");