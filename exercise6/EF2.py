for a in range(3, 500):
    for b in range(a+1, 500):
        for c in range(b+1, 500):
            if a**2 + b**2 == c**2:
                print(a, b, c, sep=',')
                break
