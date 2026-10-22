'''
Uma escola está organizando os dados dos alunos para criar um relatório resumido. Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:


Copiar
Aluno: Nome
Idade: Idade
Nota: Nota
'''

info = input("Informe o nome, idade e nota separados por virgula: ").lower().split(", ")
for x in range (0, len(info),3):
    aluno, idade, nota = info[x], info[x+1], info[x+2]
    print(f"Aluno: {aluno}\nIdade: {idade}\nNota: {nota}\n\n")