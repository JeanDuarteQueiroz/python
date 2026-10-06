#Exibir números de uma lista usando um loop

# Dada uma lista de números, percorra-a e imprima os números que satisfazem as seguintes condições:

#O número deve ser divisível por cinco.
#Se o número for maior que 150, pule e passe para o próximo.
#Se o número for maior que 500, interrompa o loop completamente.
numeros = [12, 75, 150, 180, 145, 525, 50];
listaNova = [];
for x in range(0,len(numeros),1):
    if numeros[x] > 500:
        print(f" {numeros[x]} ultrapassou o limite estabelecido. Fica de Fora!");
        break
    elif numeros[x] > 150:
        continue
    elif numeros[x] % 5 == 0:
        listaNova.append(numeros[x]);
    else:
        print(f" {numeros[x]} não é um número válido. Fica de Fora!");

print(f" A nova lista é: {listaNova}");   