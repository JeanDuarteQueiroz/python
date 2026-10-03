

def pegaFatorial (numero):
    fatorial = 1;
    for x in range(1,numero+1):
        fatorial = fatorial * x; 
    return fatorial
print(pegaFatorial(5))