def somaRecursiva (n):
    if n == 1:
        return 1
    return n + somaRecursiva(n-1)
    
print(somaRecursiva(5))