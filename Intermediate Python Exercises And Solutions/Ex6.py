'''
Practice Problem: Given a sentence, reverse each individual word within the string while maintaining the original word order

Given Input: "Python is awesome"

Expected Output: "nohtyP si emosewa"
'''

def reverte_frase (frase):
    tmp = frase.split()
    
    invertida = [word[::-1] for word in tmp]

    return " ".join(invertida)
    
print(reverte_frase("Python is awesome"))