a = [10,20,30,40,20,10,50,50,10,30]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)