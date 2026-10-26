'''
Tendo como dados de entrada um arquivo em Gigabytes,
construa um algoritmo que faça a conversão para Megabytes,
usando a seguinte fórmula:
Gigabytes * 1024
'''

tamanho = float(input("Digite o tamanho do arquivo em GBs:  "))
print(f"O tamanho em Megabytes é {tamanho *1024:.1f}")
