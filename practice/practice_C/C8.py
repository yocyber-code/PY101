for i in range(1, 11):
    for j in range(1, 11-i):
        print('-', end='')
    if i % 2 == 0:
        start = 1
        stop = i + (1*i)
        step = 1
    else:
        start = i + (1*i) - 1
        stop = 0
        step = -1
    for j in range(start, stop, step):
        print(j, end='')
    print()
