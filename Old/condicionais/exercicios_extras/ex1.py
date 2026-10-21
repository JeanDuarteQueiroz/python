bpm = int(input("Informe seus batimentos por minuto(bpm):  "));
idade = int(input("Informe a sua idade:  "));

if (idade) <= 2:
    print("Vamos verificar seus batimentos");
    if (bpm) < 120:
        print("Está ABAIXO da faixa esperada");
    elif (bpm) > 140:
        print("Está ACIMA da faixa esperada");
    else:
        print("Está dentro da faixa esperada");
elif (idade) >= 8 and (idade) <=17:
    print("Vamos verificar seus batimentos");
    if (bpm) < 100:
        print("Está ABAIXO da faixa esperada");
    elif (bpm) > 120:
        print("Está ACIMA da faixa esperada");
    else:
        print("Está dentro da faixa esperada");
elif (idade) > 17 and (idade) <= 60:
    print("Vamos verificar seus batimentos");
    if (bpm) < 70:
            print("Está ABAIXO da faixa esperada");
    elif (bpm) > 80:
            print("Está ACIMA da faixa esperada");
    else:
            print("Está dentro da faixa esperada");
elif (idade) > 60:
    print("Vamos verificar seus batimentos");
    if (bpm) < 50:
        print("Está ABAIXO da faixa esperada");
    elif (bpm) > 60:
        print("Está ACIMA da faixa esperada");
    else:
        print("Está dentro da faixa esperada");
else:
    print("Não entendi sua idade!");