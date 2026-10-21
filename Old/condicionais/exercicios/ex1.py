# O doutor Henry Jones Junior estabeleceu uma regra com seus alnos da disciplina de Arqueologia: todos os que obtiverem nota maior do que 8,5 na sua prova semestral serão convidados para uma visita de campo na América do Sul.
# Nosso programa deve solicitar o e-mail e a nota do aluno, exibindo a mensagem "ENVIANDO CONVITE" caso a nota do aluno satisfaÇã a condição proposta.
#Utilizando apenas um if simples, podemos resolver esse problema rapidamente! Basta solicitarmos a digitação dos dados, converter a nota para reais e verificar se ela atende à condição do professor Jones.


email, nota = input("Informe o seu e-mail:  ").upper(), float(input("Infomre a sua nota:  "));

if (nota) >= 8.5:
    print("ENVIANDO CONVITE PARA {}".format(email));
else:
    print("Não atingiu a nota suficiente!");
