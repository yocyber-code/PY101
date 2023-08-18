import math

n = int(input())
arr = []
while len(arr) < n:
    arr.append(int(input()))

arr_result = []
for i in range(math.ceil(len(arr) / 2)):
    if i == math.ceil(len(arr) / 2):
        arr_result.append(arr[i]*2)
    else:
        arr_result.append(arr[i] + arr[len(arr) - i - 1])
print(arr_result)
