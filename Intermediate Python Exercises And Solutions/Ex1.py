'''
Practice Problem: 
Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.

Given Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]

Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']
'''

list = ["apple", "bat", "cherry", "dog", "elderberry"]

new_list = [w.upper() for w in list if len(w) >= 4]

print(new_list)