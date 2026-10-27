'''
Practice Problem: 
Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.

Given Input: nested = [1, [2, 3], [4, [5, 6]], 7]

Expected Output: Flattened: [1, 2, 3, 4, 5, 6, 7]
'''
flattened = []
def achatar_lista (lista):
    for x in lista:
        if type(x) == list:
            achatar_lista(x)
        else:
            flattened.append(x)
    
    return flattened

nested = [1, [2, 3], [4, [5, 6]], 7]

new = achatar_lista(nested)
print(new)