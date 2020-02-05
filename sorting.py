def sort_list(data_list):
    new_list = []

    while data_list:
        min = data_list[0]

        for i in data_list:
            if i < min:
                min = i
        new_list.append(min)
        data_list.remove(min)
    return new_list

a = [10,40,23,65,34,89,67,48]
b = sort_list(a)
print(b)