for i in range(1, 11):
    for j in range(i + 9, 0, -1):
        if (j <= i + 1 * i - 1):
            print('x', end='')
        else:
            print('-', end='')
    print()
