'''
    Exercício:
    Usando um laço WHILE, conte os dígitos de um número inteiro.         
'''

def separaNum (num):
    numero =num;
    count =0;
    while numero != 0:
        numero = numero // 10;
        count += 1;
    return count

num = separaNum(int(input("Digite uns números ai:  ")));

# num = int(len(input("Digite uns numeros:  ")));
print("A quantidade de dígitos é: ", num);


    