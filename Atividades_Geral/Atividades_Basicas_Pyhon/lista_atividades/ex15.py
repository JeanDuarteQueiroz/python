'''
Practice Problem: Write a program to find the largest and smallest digit within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).

Exercise Purpose: This combines Digit Extraction (from Exercise 14) with Min/Max Comparison. It’s a foundational logic for finding “extremes” in a dataset. You learn how to initialize comparison variables and update them dynamically as you scan through data.

Given Input: num = 75869
'''

def maiorMenor (string):
    maior=0;
    menor=9;
    num = int(string);
    while num > 0:
         digit = num % 10;
         if digit > maior:
             maior = digit
         elif digit < menor:
             menor = digit;
         num = num // 10;
    return  maior, menor

maior, menor = maiorMenor(input("Digite um número:  "));
print(maior, menor);