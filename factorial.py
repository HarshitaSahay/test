n = 5
fact = 1
for i in range(1, n+1):
    fact = i * fact

print(fact)

def factorial(a):
    fact1 = 1
    if a==0 or a==1:
        fact1 = 1
    else:
       for x in range(1, a+1):
           fact1 = fact1*x
    return fact1

print(factorial(6))