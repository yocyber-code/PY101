for i in range(10, 0, -1):
    for j in range(0, 10, 1):
        if(j > i - 2):
            print('x', end='')
        else:
            print('-', end='')
    print()
