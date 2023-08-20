while True:
    n = int(input())
    if n == -1:
        print("exit")
        break
    if n < 10000:
        print(0.0)
    elif n >= 25000:
        print(n * 0.1)
    else:
        print(n * 0.07)
