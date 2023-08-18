n = 5
for i in range(n - 1, -1, -1):
    for j in range(0, n + i):
        if j < n - i - 1:
            print("-", end='')
        else:
            print("x", end='')
    print()
