for i in range(1, 1001):
    count = 0
    if i % 3 == 0:
        count += 1
    if i % 5 == 0:
        count += 1
    if i % 7 == 0:
        count += 1
    if count == 2:
        print(i)
