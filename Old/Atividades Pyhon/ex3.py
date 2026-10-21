
import random

numero_sorteado = 0;
palpite = -1;

while palpite != numero_sorteado:
    numero_sorteado = random.randint(1, 10);
    palpite = int(input("Digite um número:  "));
    if palpite == numero_sorteado:
        print("Bom palpite!");
    else:
        print("Tente novamente!");

