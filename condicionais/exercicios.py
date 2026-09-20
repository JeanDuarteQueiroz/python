## if simples ##

name = input("Informe o seu nome:  ");
idade = input("Informe sua idade:  ");

if int(idade) >= 18:
    print("Uau, {}!, você é maior de idade!!".format(name))
else:
    print("Logo você vai ser maior de idade!")



## if encadeado ##

name = input("Informe o seu nome:  ");
idade = input("Informe a sua idade:  ");

if int(idade) >= 18:
    print("Uau, {}! você é maior de idade!".format(name));
    carteira = input("Já fez a carteira de habilitação?  S-SIM, N-NÃO");
    if (carteira) == "S":
        print("Que maneiro!");
    else:
        print("Não esquenta! Logo você consegue!");
else:
    print("Logo você vai ser maior de idade!");