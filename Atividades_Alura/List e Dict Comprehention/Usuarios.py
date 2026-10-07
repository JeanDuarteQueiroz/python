''' 
Classificando usuários com base na idade

Você trabalha como cientista de dados em uma empresa que armazena informações sobre seus usuários. Foi solicitado que você crie uma classificação simples dos usuários com base na idade. A classificação deve ser feita em duas categorias:

"adulto": Para usuários com 18 anos ou mais.
"menor": Para usuários com menos de 18 anos.
Os dados dos usuários estão armazenados em um dicionário chamado usuarios, no seguinte formato:

usuarios = {
    "João": 25,
    "Maria": 17,
    "Ana": 19,
    "Carlos": 16,
    "Beatriz": 22,
    "Pedro": 15,
    "Luiza": 18
}

Usando dict comprehension com if e else, crie um novo dicionário chamado classificacao_usuarios, onde:

As chaves serão os nomes dos usuários.
Os valores serão as strings "adulto" ou "menor", dependendo da idade.
O dicionário resultante deve ter o seguinte formato:

{
    "João": "adulto",
    "Maria": "menor",
    "Ana": "adulto",
    "Carlos": "menor",
    ...
}
'''

usuarios = {
    "João": 25,
    "Maria": 17,
    "Ana": 19,
    "Carlos": 16,
    "Beatriz": 22,
    "Pedro": 15,
    "Luiza": 18
}

classificacao_usuarios = {
    nome: "Adulto" if idade >= 18 else "Menor"
    for nome, idade in usuarios.items()
}

print ("Essa é a classificação dos usuários: \n", classificacao_usuarios);