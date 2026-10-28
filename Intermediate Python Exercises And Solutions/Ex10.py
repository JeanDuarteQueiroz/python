'''
Practice Problem: Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’

Given Input: List: [1, 2, 3, 4, 5], Shift: 2, Direction: 'right'

Expected Output: [4, 5, 1, 2, 3]
'''

def rotate_list(lst, n, direction):
    if n > len(lst):
        n = n % len(lst)
    list_tmp = []
    rotate_list = []
    if direction == "right":
        indice = len(lst) - (n-1)
        list_tmp = [x for x in lst if x < indice]
        rotate_list = [x for x in lst if x >= indice]
    elif direction == "left":
        indice = n
        list_tmp = [x for x in lst if x < indice]
        rotate_list = [x for x in lst if x >= indice]
    else:
        print("Right or Left!")
        
    rotate_list.extend(list_tmp)
    return rotate_list

list = [1, 2, 3, 4, 5]
n = int(input("Corte em qual? "))
direction = input("Right or Left? ").lower().strip()

print(rotate_list(list, n, direction))