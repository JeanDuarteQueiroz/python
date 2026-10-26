'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanho = float(input("Digite o tamanho do arquivo em MB:  "))
velocidade = float(input("Digite a velocidade da internet em MB por segundo:  "))

print(f"O tempo aproximado para download é {(tamanho/velocidade)/60:.2f} minutos")