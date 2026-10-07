'''
Análise de dados de atletas em uma lista

Você é um cientista de dados trabalhando para um comitê olímpico. 
Você recebeu uma lista com informações de atletas de diversas modalidades, incluindo nome, altura (em metros) e peso (em kg). 
Esses dados estão organizados de forma um pouco confusa, dificultando a análise. 
Sua tarefa é usar um loop for em Python para processar essa lista e organizar as informações de cada atleta em um formato mais estruturado, 
facilitando futuras análises estatísticas e comparações.

Objetivo:
Utilizando um loop for, crie um programa que processe a lista atletas e para cada atleta, imprima as informações no seguinte formato:

Nome: <Nome do Atleta>
Altura: <Altura do Atleta> m
Peso: <Peso do Atleta> kg
--------------------

A lista de atletas é representada da seguinte maneira:
'''



pre_atletas = [

    ["Maria Silva", 1.75, 65],
    ["João Santos", 1.80, 72],
    ["Ana Pereira", 1.68, 58],
    ["Pedro Oliveira", 1.92, 85],
    ["Carlos Lima", 1.85, 78],
    ["Beatriz Souza", 1.70, 60],
    ["Fernanda Costa", 1.62, 55],
    ["Lucas Almeida", 1.88, 82],
    ["Rafaela Gomes", 1.74, 63],
    ["Gustavo Ferreira", 1.90, 88],
    ["Larissa Rocha", 1.66, 57],
    ["Henrique Nunes", 1.83, 76],
    ["Juliana Martins", 1.72, 90],
    ["Ricardo Carvalho", 1.86, 80],
    ["Sofia Alves", 1.64, 54],
    ["Matheus Ribeiro", 1.89, 84],
    ["Camila Duarte", 1.69, 81],
    ["Gabriel Monteiro", 1.77, 73],
    ["Eduarda Farias", 1.71, 62],
    ["Thiago Mendes", 1.84, 79],
]

def exibeInfoAtletas (atletas):
    for x in pre_atletas:
        print(f"Nome: {x[0]}\nAltura: {x[1]}m\nPeso: {x[2]}Kg");
        print("-" * 20);
        
'''
Criando uma lista de tuplas

Continuando o seu trabalho como cientista de dados do comitê olímpico, agora você deve reorganizar a lista de atletas, em uma lista de tuplas, 
onde cada tupla representa um atleta e contém as informações de nome, altura e peso, respectivamente. 
Essa estrutura permitirá o acesso aos dados de cada atleta de forma mais eficiente, e que esses dados não possam mais ser modificados. 
Essa organização é crucial para etapas posteriores da análise, como o cálculo do IMC (Índice de Massa Corporal) de cada atleta e a identificação de padrões nos dados.

Objetivo:

Escreva um programa Python que converta a lista atletas em uma lista de tuplas, onde cada tupla contém o nome, altura e peso de um atleta. 
Imprima a lista de tuplas resultante.
'''

def infoAtletasTupla (atletas):
    atletas = []
    for x in pre_atletas:
        nome = x[0];
        altura = x[1];
        peso = x[2];
        i_atleta = (nome, altura, peso);
        atletas.append(i_atleta);
    return atletas

listaAtletas = infoAtletasTupla(pre_atletas)



'''
Usando o list comprehension

Estamos trabalhando com o conjunto de dados contendo informações sobre atletas, já no formato de tuplas.

Para uma análise preliminar, precisamos calcular a altura média desses atletas de forma eficiente utilizando o recurso de list comprehension
do Python. Esses dados são cruciais para entender as características físicas gerais do grupo de atletas e podem ser usados posteriormente
para comparações com outros grupos ou para identificar padrões interessantes.

Objetivo:
Utilizando list comprehension calcule e imprima a altura média desses atletas.
'''

alturas = [atleta[1] for atleta in listaAtletas];

mediaAlturas = sum(alturas) / len(alturas)

print(f"A altura média dos participantes é:  {mediaAlturas:.2f}");

'''

Calculando o IMC

Estamos trabalhando com uma versão atualizada do conjunto de dados contendo informações sobre atletas, já no formato de tuplas.

Agora, queremos identificar quais atletas possuem IMC (Índice de Massa Corporal) acima de 25, que é considerado como sobrepeso. O cálculo do IMC pode ser feito com a fórmula:

Fórmula do IMC: IMC = peso / altura².

Utilizando list comprehension, crie uma lista contendo o nome dos atletas que possuem IMC maior que 25 e imprima essa lista.

'''

imcMaior = [
    [atleta[0] 
     for atleta in listaAtletas 
     if (atleta[2] / (atleta[1]**2)) > 25]
]
print("Atletas com sobrepeso: ")
print(imcMaior)


'''
Classificando o IMC

Estamos trabalhando com o mesmo conjunto de dados contendo informações sobre atletas, já no formato de tuplas.

Queremos classificar os atletas com base em seu IMC (Índice de Massa Corporal) como "Peso Normal" ou "Sobrepeso". Porém, dessa vez queremos uma lista mais elaborada. O cálculo do IMC pode ser feito com a fórmula:

'''

listaIMC = [
    (atleta[0], "Peso Normal" if (atleta[2] / (atleta[1]**2)) < 25 else "Sobrepeso")
    for atleta in listaAtletas
]

print("Classificação dos atletas:\n", listaIMC);
