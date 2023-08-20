n = 9
for i in range(n):
    for j in range(n * 2):
        if i < n/2:
            if j <= i + (1 * i) or j >= (n * 2 - 1) - (i + (1 * i)):
                print("*", end="")
            else:
                print("-", end="")
        else :
            if j > i + (1 * i) or j < (n * 2 - 1) - (i + (1 * i)):
                print("*", end="")
            else:
                print("-", end="")
    print()
