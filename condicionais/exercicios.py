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
else:
    print("Logo você vai ser maior de idade!");
    carteira = input("Você quer fazer carteira?  S-SIM ou N-NÃO  "); 
    if (carteira) == 'S': #Sensitive-case# 
        print("Que maneiro!!");
    else:
        print("Showww");


## elif ##

name = input("Qual é o seu nome?  ");
idade = input("Qual é a sua idade?  ");

if int(idade) >= 18:
    print("Uau, você já é maior de idade!");
elif int(idade) == 17:
    print("Você já é quase de maior!");
elif int(idade) == 16:
    print("Você está deixando de ser adolecente!");
else:
    print("Você ainda é adolecente!");
    
