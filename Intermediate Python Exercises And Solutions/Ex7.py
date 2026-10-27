'''
Practice Problem: Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.

Given Input: "A man, a plan, a canal: Panama"

Expected Output: True
'''

def verifica_palindromo(str):
    str_clean = [char.lower() for char in str if char.isalnum()]
    print(type(str_clean))
    str_str = " ".join(str_clean)
    return str_str == str_str[::-1]

    # tmp = list(str)
    # new_list = ''
    
    # for x in tmp:
    #     if x.isalnum():
    #         new_list += x.lower()
            
    # reverse_list = new_list[::-1]     
    # return new_list == reverse_list

frase = "Was it a car or a cat i saw"
print(verifica_palindromo(frase))