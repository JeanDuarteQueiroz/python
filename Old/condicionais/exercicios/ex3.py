# Transporte-se no tempo e volte para a época da escola! Lembra do dia em que aprendeu o valor de X nas equações de 2° grau? Aquelas que tinham uma carinha parecida com Ax² + Bx + C = 0?
# Aquela fórmula que aprendemos como fórmula de Bhaskara (mas que não foi ele quem criou) deixou saudades (ou pesadelos terríveis).
# Vamos dar um presente ao seu "eu" do passado e criar um programa no qual o usuário só tenha que descrever os valores de A, B e C e nosso programa vai se encarregar de fazer os cálculos.
# A primeira etapa que aprendemos na escola é calcular o *delta* por meio da fórmula: B² -4 . A . C e depois, caso o delta seja positivo, existem dois valores para x. Caso seja zero, existe apenas um valor. E caso seja negativo, informamos que não há valor real para X.
import math;

a, b, c = float(input("Informe o valor de A:  ")), float(input("Informe o valor de B:  ")), float(input("Informe o valor de C:  "));

valor_delta = (b * b) - 4 * a * c;
print("O valor de delta é: {}".format(valor_delta));

if (valor_delta) > 0.0:
    x1 = (- b + math.sqrt(valor_delta)) / (2 * a)
    x2 = (- b - math.sqrt(valor_delta)) / (2 * a)
    print("Existem dois valores para X, os valores são: X1= {} e X2= {}".format(x1, x2));        
elif (valor_delta) == 0.0:
    x = (- b + math.sqrt(valor_delta)) / (2 * a)
    print("Existe apenas um valor para X, o valor é: {}".format(x));
else:
    print("Não há valor real para X");