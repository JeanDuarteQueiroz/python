soma = lambda x, y: x+y;
subtracao = lambda x,y: x-y;
multiplicacao = lambda x,y: x*y;
divisao = lambda x,y: x/y;

x = float(input("Digite um número:  "));
y = float(input("Digite outro número:  "));
op = input("Digite o operador matematico ( | + | - | * | / | ):  ");

operacoes = {
    "+": soma,

    "-": subtracao,
    
    "*":  multiplicacao,
    
    "/": divisao
}

if op in operacoes:
    if op == "/" and y == 0:
        print("Erro! Divisão por zero.");
    print(f"O resultado é: {operacoes[op](x,y)}");
else:
    print("Operador matematico inválido.")