#Crie uma lista chamada frutas contendo os elementos "maçã", "banana" e "laranja". Em seguida, faça o seguinte:

frutas = ["maça", "banana", "laranja"];

#Adicione a fruta "uva" ao final da lista.

frutas.append("uva");

#Insira a fruta "morango" na primeira posição

frutas.insert(0,"morango");

#Remova a fruta "banana" da lista.

frutas.pop(2);

#Imprima o tamanho total da lista e o resultado final.

total = len(frutas);#len retorna a quantidade de objetos dentro de uma lista;
print(total);
print(frutas);