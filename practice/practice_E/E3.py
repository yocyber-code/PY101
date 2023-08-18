a = int(input())
b = int(input())
result = max(a, b)
step = 2 if a % 2 == 0 and b % 2 == 0 else 1
while True:
    if (result % a == 0 and result % b == 0):
        print(result)
        break
    result += step
