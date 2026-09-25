tupla = ("apple", "banana", "cherry", "date");

#print(f"O primeiro item é '{min(tupla)}', o último item é '{max(tupla)}' e o tamanho total da lista é: '{len(tupla)}'")

primeiro = None;
ultimo = None;

for x in range(len(tupla)):
    
    if x == 0:
        primeiro = tupla[x];
    elif x == len(tupla) -1:
        ultimo = tupla[x];
        
print(f"O primeiro item  é: {ultimo}\nO último item é: {primeiro}")


## esperar quando os exercicios cobrarem a leitura da tupla