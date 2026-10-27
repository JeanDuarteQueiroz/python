'''
Practice Problem: Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.

Given Input: "A man, a plan, a canal: Panama"

Expected Output: True
'''

def verifica_palindromo(str):
    str_clean = [char.lower() for char in str if char.isalnum()]
    str_str = " ".join(str_clean)
    
    return str_str == str_str[::-1]

frase = "Was it a car or a cat i saw"
print(verifica_palindromo(frase))