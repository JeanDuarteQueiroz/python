'''
Practice Problem: Write a program to check if a given number is a palindrome. A palindrome number is a number that remains the same when its digits are reversed (e.g., 121, 343).

Exercise Purpose: This exercise combines Mathematical Reversal with Conditional Comparison. It teaches storing an original value before modifying it in a loop so you can perform a final validation.

Given Input: number = 121

Expected Output: Yes
'''

def ePalindromo (numero):
    num = int(numero);
    numero_reverso = 0;
    while num > 0:
        digit = num % 10;
        numero_reverso = (numero_reverso * 10) + digit;
        num = num // 10;
    if str(numero_reverso) != numero:
        return False
    elif str(numero_reverso) == numero:
        return True
    else:
        print("Socorro! Chame o suporte!");
    return

palindromo = ePalindromo(input("Digite um número:  "))
print(palindromo);
