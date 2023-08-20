a = int(input())
b = int(input())
c = int(input())
m = int(input())

if m > 5:
    y = a * m * 2 + b * m + c
elif m < 5:
    y = a * m * 2 + b * m
else:
    y = a * m * 2 + b * m - c
print(y)
