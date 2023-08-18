arr = []
while len(arr) < 10:
    arr.append(int(input()))
result = 1
for i in arr:
    result *= i
print(result)