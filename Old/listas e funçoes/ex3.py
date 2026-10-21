# Dada uma lista de notas de um aluno:

notas = [7.5, 8.0, 6.0, 9.5, 5.0];

#Sem usar funções prontas do Python como sum(), max() ou min() (use laços de repetição):

#Calcule e exiba a média das notas.

def pegaMedia (notas):
    total = 0;
    for x in range(0,len(notas),1):
        total = total + notas[x]; 
    media = total / len(notas);
    return media
#Encontre e exiba a maior e a menor nota.

def pegaMaioreMenor (notas):
    menor = 10;
    maior = 0;
    for x in range(0,len(notas),1):
        if notas[x] > maior:
            maior = notas [x];
        elif notas[x] < menor:
            menor = notas[x];
    return maior, menor;

mediaNota = pegaMedia(notas);
print(f"A média das notas é: {mediaNota}");

maiorNota, menorNota = pegaMaioreMenor(notas);
print(f"A maior nota é: {maiorNota}\nA menor nota é: {menorNota}");