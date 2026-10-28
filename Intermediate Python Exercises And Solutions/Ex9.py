'''
Practice Problem: Write a function that removes duplicate elements from a list. You cannot use set() because sets do not maintain the original order of elements.

Given Input: [1, 2, 2, 3, 1, 4, 2]

Expected Output: [1, 2, 3, 4]
'''

def remove_duplicate(list):
    new_list = []
    for x in list:
        if x not in new_list:
            new_list.append(x)
        else:
            continue
    return new_list

list = [1, 2, 2, 3, 1, 4, 2]
print(remove_duplicate(list))