def rec(n):
    if (n == 0):
        return
    print('x', end='')
    rec(n - 1)


for i in range(0, 10):
    rec(10)
    print()
