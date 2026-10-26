'''
Practice Problem: 
Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.

Given Input: text = "Python Programming"

Character Frequency: 
Counter({'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'a': 1, 'g': 2, 'm': 2, 'i': 1})
'''

from collections import Counter

def count_input(text):
    
    clean = text.lower().replace(" ", "")
    
    return Counter(clean)

text = input("Digite uma frase: ")
text_clean = count_input(text)
print(text_clean)