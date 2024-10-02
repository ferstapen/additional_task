def calculate_structure_sum(data):
    summa = 0
    if isinstance(data, dict):
        for i, j in data.items():
            summa += calculate_structure_sum(i)
            summa += calculate_structure_sum(j)
    elif isinstance(data, (set, tuple, list)):
        for i in data:
            summa += calculate_structure_sum(i)
    elif isinstance(data, int):
        summa += data
    elif isinstance(data, str):
        summa += len(data)
    return summa

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)



