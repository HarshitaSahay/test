test_list = ['Arham', 'Anand', 'manjeet', 'ranjeet', 'ravinder']

check = 'et'
result_list = []

for name in test_list:
    if name.endswith(check.lower()):
        result_list.append(name)

print(result_list)
