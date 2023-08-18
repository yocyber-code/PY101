def rec(n):
    if (n == 0):
        return
    print('x', end='')
    rec(n - 1)

rec(10)
