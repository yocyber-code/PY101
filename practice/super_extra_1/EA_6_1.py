n = 5
for i in range(0, n):
    for j in range(0, n + i):
        if j < n - i - 1:
            print("-", end='')
        else:
            print("x", end='')
    print()
