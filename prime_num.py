def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, " is not prime")
                break
        else:
            print(num, " is a prime number")
    else:
        print(num, " is not prime")

is_prime(5)
is_prime(11)
is_prime(20)
is_prime(2)