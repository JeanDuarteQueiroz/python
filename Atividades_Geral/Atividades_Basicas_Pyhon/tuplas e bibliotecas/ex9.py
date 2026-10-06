votacao = ("yes", "yes", "no", "yes", "no", "no", "yes");

resultado = {};

def pegaVoto (lista):
    resultado = {};
    for x in lista:
        if x in resultado.keys():
           resultado[x] += 1
        else:
           resultado[x] = 1
    return resultado;

resultado = pegaVoto(votacao);
print(f"Esse é o resultado: \n{resultado}")

