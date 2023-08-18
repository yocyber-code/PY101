print("2")

for i in range(3, 100, 2):
    is_prime = True
    for j in range(3, int(i/2), 2):
        if (i % j == 0):
            is_prime = False
            continue
    if (is_prime):
        print(i)
