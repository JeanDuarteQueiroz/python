'''
Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

Para Megabytes: Gigabytes * 1024
Para Kilobytes: Gigabytes * 1024 * 1024
Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.

'''

tamanho = float(input("Digite o tamanho do arquivo em GBs:  "))
print(f"O tamanho em Megabytes é {tamanho * 1024:.1f} e em Kilobytes é {(tamanho *1024)*1024:.1f}")