import math

n = int(input())
extra = 0
i = 0
step = 1
if (n % 2 == 0):
    extra = 1
while i > -1:
    j = 0
    for j in range(0, n - extra):
        if j == math.floor(n/2) - i - extra or j == math.floor(n/2) + i - extra:
            print('x', end='')
        else:
            print('-', end='')
    print()
    i += step
    if (n == 1):
        break
    if (i > (math.ceil(n/3) + int(n / 16) if n >= 9 else math.floor(n / 5))):
        step = -1
