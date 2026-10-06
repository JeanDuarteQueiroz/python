def contaVogalConsoante (texto):
    vogais = ['a','e','i','o','u'];
    eVogal = [];
    eConsoante = []; 
    for x in texto.lower():
        if x.isalpha():
            if x in vogais:
                eVogal.append(x);
            else:
                eConsoante.append(x);
    return eVogal, eConsoante;

vogal, consoante = contaVogalConsoante(input("Digite ai:  "));

print(f" O número de Vogais é ",len(vogal)," e elas são ",vogal);
print(f" O número de Consoantes é ",len(consoante)," e elas são ",consoante)