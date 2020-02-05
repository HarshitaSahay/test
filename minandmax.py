def min_max(data_list):
    min = data_list[0]
    max = data_list[0]

    for i in data_list:
        if i < min:
            min = i
        elif i > max:
            max = i
    return [min,max]

a = [23, 19, 42, 88, 65, 100, 54, 11]
print(min_max(a))