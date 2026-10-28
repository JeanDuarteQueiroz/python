'''
Practice Problem: Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).

Given Input: ["apple", "education", "ice", "ocean", "python", "umbrella"]

Expected Output: ['education', 'umbrella']
'''

def filtro_lista(lista):
    lista_filtrada = [word for word in lista if len(word) > 5 and word[0] in "aeiou"]
    return lista_filtrada

lista = ["apple", "education", "ice", "ocean", "python", "umbrella"]

print(filtro_lista(lista))