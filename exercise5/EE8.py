m = int(input())
n = int(input())

if m >= n:
    for i in range(m, n-1, -1):
        if i == n:
            print(i)
        else:
            print(i, end=',')
