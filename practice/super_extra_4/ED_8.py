def is_prime(number):
    if (number == 1 or number % 2 == 0):
        print(1)
        return
    elif (number == 2):
        print(0)
        return
    for i in range(3, int(number/2), 2):
        if (number % i == 0):
            print(1)
            return
    print(0)


number = int(input())
is_prime(number)
