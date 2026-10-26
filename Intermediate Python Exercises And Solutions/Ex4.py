'''
Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).

Given Input: word1 = "listen", word2 = "silent"

Expected Output: Is "listen" an anagram of "silent"? True
'''

def valida_anagrama(w1, w2):
    t1 = sorted(w1.lower().strip())
    t2 = sorted(w2.lower().strip())
    return t1 == t2

w1 = "listen "
w2 = " silent"
result = valida_anagrama(w1, w2)
print(f'Is "{w1}" an anagram of "{w2}"? . . . {result}')