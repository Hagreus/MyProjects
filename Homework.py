dict_1 = {'a': 2, 'b': 4, 'c': 6}
dict_2 = {'b': 6, 'a': 8, 'c': 4, 'd': 10}

for k, v in dict_2.items():
    if k in dict_1:
        dict_1[k] = dict_1[k] + dict_2[k]
    else:
        dict_1[f'{k}'] = dict_2[k]

print(dict_1)