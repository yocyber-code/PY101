arr = []
while len(arr) < 10:
    arr.append(int(input()))
arr.sort()
print(arr[len(arr) - 2])
