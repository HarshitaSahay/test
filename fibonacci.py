def fibonacci(nterms):
    n1, n2 = 0,1
    count = 0
    if nterms <= 0:
        print("Invalid input. Please enter a positive number.")
    elif nterms == 1:
        print("Fibonacci series upto 1: ", n1)
    else:
        print("Fibonacci series")
        while count<nterms:
            print(n1)
            temp = n1 + n2
            n1 = n2
            n2 = temp
            count += 1

n = int(input("Enter the number of terms: "))
fibonacci(n)