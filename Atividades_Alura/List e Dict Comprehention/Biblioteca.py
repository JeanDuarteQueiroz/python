'''
Você é responsável pelo setor de tecnologia de uma biblioteca pública e está trabalhando em um sistema de categorização de livros com base no ano de publicação. 
A lista de livros da biblioteca está no seguinte formato:
'''
livros = [
    ("Dom Quixote", 1605),
    ("Orgulho e Preconceito", 1813),
    ("O Grande Gatsby", 1925),
    ("Cem Anos de Solidão", 1967),
    ("1984", 1949),
    ("Harry Potter e a Pedra Filosofal", 1997),
    ("O Senhor dos Anéis", 1954),
    ("A Revolução dos Bichos", 1945),
    ("O Apanhador no Campo de Centeio", 1951),
    ("O Código Da Vinci", 2003),
    ("Jogos Vorazes", 2008),
    ("A Culpa é das Estrelas", 2012),
    ("Duna", 1965),
    ("A Menina que Roubava Livros", 2005),
    ("O Hobbit", 1937),
    ("Moby Dick", 1851),
    ("Drácula", 1897),
    ("Frankenstein", 1818),
    ("A Odisséia", -800),  # Ano fictício para livros clássicos antigos
    ("Hamlet", 1600),
]
'''
Agora, você precisa classificar os livros em duas categorias:

"Clássico": Livros publicados antes do ano 2000.
"Moderno": Livros publicados no ano 2000 ou depois.
Utilizando list comprehension com if e else, crie uma nova lista contendo tuplas no formato:
(título_do_livro, "Clássico" ou "Moderno")
'''

livro_class = [
    (titulo[0], "Clássico" if titulo[1] < 2000 else "Moderno")
    for titulo in livros
]

''' 
Organizando livros em um dicionário

Você está trabalhando na mesma lista de livros:
'''
livros_2 = [

    ("Dom Quixote", "Miguel de Cervantes", 1605),

    ("Orgulho e Preconceito", "Jane Austen", 1813),

    ("O Grande Gatsby", "F. Scott Fitzgerald", 1925),

    ("Cem Anos de Solidão", "Gabriel García Márquez", 1967),

    ("1984", "George Orwell", 1949),

    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997),

    ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),

    ("A Revolução dos Bichos", "George Orwell", 1945),

    ("O Apanhador no Campo de Centeio", "J.D. Salinger", 1951),

    ("O Código Da Vinci", "Dan Brown", 2003),

]
'''

Seu objetivo é criar um dicionário onde cada livro será representado por uma chave (o título do livro)
e o valor será outro dicionário contendo as informações do autor e do ano de publicação. O dicionário final deve ter o seguinte formato:

{
    "Dom Quixote": {"autor": "Miguel de Cervantes", "ano": 1605},
    "Orgulho e Preconceito": {"autor": "Jane Austen", "ano": 1813},
    "O Grande Gatsby": {"autor": "F. Scott Fitzgerald", "ano": 1925},
    ...
}
'''



livros_info = {
    titulo[0]:{"Autor": titulo[1], "Ano": titulo[2] }
    for titulo in livros_2
}

print(livros_info)

livros_antigos = {
    nome: {
        "Autor": dados["Autor"], 
        "Ano": dados["Ano"]
    }
    for nome, dados in livros_info.items()
    if dados["Ano"] < 2000
}

print("Esses são os livros antigos: \n", livros_antigos)


''' 
Atualizando os anos dos livros


Você recebeu uma solicitação para atualizar o dicionário catalogo, pois agora todos os anos de publicação dos livros devem ser convertidos para o número de anos que se passaram desde o lançamento até o ano atual (2025).

O dicionário original catalogo tem o seguinte formato:

Usando dict comprehension, crie um novo dicionário chamado livros_atualizados, onde cada livro terá o mesmo título e autor, mas o campo "ano" será substituído pelo número de anos que se passaram desde o lançamento até 2025.

O dicionário resultante deverá ter o seguinte formato:
{
    "Dom Quixote": {"autor": "Miguel de Cervantes", "ano": 420},
    "Orgulho e Preconceito": {"autor": "Jane Austen", "ano": 212},
    ...
}
'''

livros_atualizados = {
    nome: {
        "Autor": dados["Autor"],
        "Ano": 2025 - dados["Ano"],
    }
    for nome, dados in livros_info.items()
}

print("Os livros atualizados ficaram assim: \n", livros_atualizados);