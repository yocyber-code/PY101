m = int(input())
n = int(input())

if m >= n:
    for i in range(n, m+1, 1):
        if i == m:
            print(i)
        else:
            print(i, end=',')
