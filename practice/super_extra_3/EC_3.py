arr = []
while len(arr) < 10:
    arr.append(int(input()))

max = -1e10
index = 0

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
        index = i
print(max)
print(index)