play = int(input("Informe quantos votos o PlayStation teve:  "));
xbox = int(input("Informe quantos votos o Xbox teve:  "));
nintendo = int(input("Informe quantos votos o nintendo teve:  "));

if (play) > xbox and (play) > nintendo:
    print("Com {} votos, o console vencedor é o PlayStation".format(play));
elif (xbox) > play and (xbox) > nintendo:
    print("Com {} votos, o console vencedor é o Xbox".format(xbox));
elif (nintendo) > play and (nintendo) > xbox:
    print("Com {} votos, o console vencedor é o Nintendo".format(nintendo));
else:
    print("Houve impate! Refaça a votação!");
