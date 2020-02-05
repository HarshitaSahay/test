# initializing list
test_list = [1, 4, None, "Manjeet", False, 4, False, 4, "Nikhil"]

# printing original list
print("The original list : ", (test_list))

# initializing K
K = 4

# using list comprehension + isinstance()
# Rear shift K in List
'''temp = [ele for ele in test_list if ele != K and ele or ele is None or isinstance(ele, bool)]
res = temp + [K] * (len(test_list) - len(temp))'''

res = []
temp = []
for i in test_list:
    if i != K and i or i is None or isinstance(i, bool):
        temp.append(i)
res = temp + [K] * (len(test_list) - len(temp))

# print result
print("The list after shifting K's to end : " + str(res))