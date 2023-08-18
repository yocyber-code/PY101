print("2")
count = 1
i = 3
while count < 100:
    is_prime = True
    for j in range(3, int(i/2), 2):
        if (i % j == 0):
            is_prime = False
    if (is_prime):
        count += 1
        print(i)
    i += 2
