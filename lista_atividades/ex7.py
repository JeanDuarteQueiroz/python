#Exibir números de uma lista usando um loop

# Dada uma lista de números, percorra-a e imprima os números que satisfazem as seguintes condições:

#O número deve ser divisível por cinco.
#Se o número for maior que 150, pule e passe para o próximo.
#Se o número for maior que 500, interrompa o loop completamente.
lista = [12, 75, 150, 180, 145, 525, 50];
resultado = [];
for x in lista:
    if x > 500:
        print(f"{x} passou do limite estabelecido! Fica fora!");
        break
    elif x > 150:
        continue
    elif x % 5 == 0:
        resultado.append(x);
    else:
        print(f"{x} não é um número válido! Fica fora!");

print(f" {resultado} ");