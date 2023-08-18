pi = 0
n = 50000
count = 1
for i in range(1, n + 1, 2):
    multiple = 1
    if(count % 2 == 0):
        multiple = -1
    else:
        multiple = 1
    pi += multiple * (1 / i)
    count += 1
print(pi * 4)