import math

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += 1/i**2
result = math.sqrt(6*sum)
print(result)
