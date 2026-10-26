'''
Practice Problem:
Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.

Given Input: dict_a = {'a': 10, 'b': 20} dict_b = {'b': 5, 'c': 15}

Expected Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}
'''

def merge_dict(d1, d2):
    result = d1.copy()
    
    for key, value in d2.items():
        result[key] = result.get(key, 0) + value
    
    return result

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

merge = merge_dict(dict_a, dict_b)
print(merge)