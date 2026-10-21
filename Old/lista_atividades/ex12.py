def contaVogaleConsoante (palavra):
    vogais = ['a','e','i','o','u'];
    ConsoantesPalavra = [];
    VogaisPalavra = [];
    for x in palavra:
        if x in vogais:
            VogaisPalavra.append(x);
        elif x == " ":
            continue;
        else:
            ConsoantesPalavra.append(x);
    return VogaisPalavra, ConsoantesPalavra;

asVogais, asConsoantes = contaVogaleConsoante(input("Digite uma palavra: ").lower());
print(f"Vogais: {asVogais} - total de {len(asVogais)} \nConsoantes: {asConsoantes} - total de {len(asConsoantes)}");