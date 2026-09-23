num_colaboradores = int(input("Informe o número de colaboradores:  "));

segunda = 0;
terca = 0;
quarta = 0;
quinta = 0;
sexta = 0;

# Laço para a quantidade de colaboradores informada.
for x in range (1,num_colaboradores + 1, 1):
    while True:  # While para não perder o voto ao digitar errado.  
        dia_semana = input("Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").lower();
        # Contagem dos votos.
        if (dia_semana) == "segunda-feira":
            segunda = segunda + 1;
            break
        elif (dia_semana) == "terça-feira":
            terca = terca + 1;
            break
        elif (dia_semana) == "quarta-feira":
            quarta = quarta + 1;
            break
        elif (dia_semana) == "quinta-feira":
            quinta = quinta + 1;
            break
        elif (dia_semana) == "sexta-feira":
            sexta = sexta + 1;
            break
        else:
            print("Opção Inválida!");

if segunda > terca > quarta > quinta > sexta:
    print(f"O dia escolido pelos colaboradores é: {segunda}");
elif terca > quarta > quinta > sexta > segunda: 
    print(f"O dia escolido pelos colaboradores é: {terca}");
elif quarta > quinta > sexta > segunda > terca:
    print(f"O dia escolido pelos colaboradores é: {quarta}");
elif quinta > sexta > segunda > terca > quarta:
    print(f"O dia escolido pelos colaboradores é: {quinta}");
elif sexta > segunda > terca > quarta > quinta:
    print(f"O dia escolido pelos colaboradores é: {sexta}");
else: 
    print("Houve empate! Refaça a votação.");