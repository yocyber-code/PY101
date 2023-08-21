pi = 0
count = 1
i = 1
prev = 0
while True:
    if (count % 2 == 0):
        multiple = -1
    else:
        multiple = 1
    pi += multiple * (1 / i)
    count += 1
    i += 2
    if (abs(pi * 4 - prev * 4) < 0.000001):
        break
    prev = pi
print(count - 1)
