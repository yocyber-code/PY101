def is_prime(number):
    if (number == 1 or number % 2 == 0):
        print("is not a prime number")
        return
    elif (number == 2):
        print("is a prime number")
        return
    for i in range(3, int(number/2), 2):
        if (number % i == 0):
            print("is not a prime number")
            return
    print("is a prime number")


number = int(input())
is_prime(number)
