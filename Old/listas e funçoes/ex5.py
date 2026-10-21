#Crie uma função chamada calculadora(a, b, operacao) que recebe dois números e uma string
#a string representando a operação ("+", "-", "*" ou "/"). 
# A função deve retornar o resultado da operação matemática correspondente. 
# Caso a operação seja inválida ou ocorra uma divisão por zero, retorne uma mensagem de erro adequada.

def calculadora(a, b, op):
    if op == "+":
        resultado = a + b;
    elif op == "-":
        resultado = a - b;
    elif op == "/":
        if b == 0:
            resultado = "Erro: Divisão por Zero";
        else:
            resultado = a / b;
    elif op == "*":
        resultado = a * b;
    else:
        resultado = "Tipo de Operação Inválida!";
    return resultado

resultado = calculadora(2,0,"x");
print(resultado);
 