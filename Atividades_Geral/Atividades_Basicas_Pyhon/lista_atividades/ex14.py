'''
Exercise 14. Reverse an integer number
Practice Problem: Write a program to reverse a given integer number (e.g., 76542 should become 24567).

Exercise Purpose: While you could convert the number to a string and slice it, doing it mathematically is more efficient and teaches you to use Modulo (%) and Floor Division (//) together to manipulate digits.

Given Input: 76542

Expected Output: 24567

'''

def reverteInteger (int):
    reversed_number = 0
    while int > 0:
        digit = int % 10
        print(digit)
        reversed_number = reversed_number * 10 + digit
        int //= 10
    return reversed_number

print(reverteInteger(76542));