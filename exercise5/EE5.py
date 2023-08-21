def is_prime(number):
    if (number == 1 or number % 2 == 0):
        return False
    elif (number == 2):
        return True
    for i in range(3, int(number/2), 2):
        if (number % i == 0):
            return False
    return True


for i in range(10000000, 3, -1):
    if (is_prime(i)):
        print(i)
        break
