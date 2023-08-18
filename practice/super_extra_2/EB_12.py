arr = []
arr.append(int(input()))
arr.append(int(input()))
arr.append(int(input()))
arr.sort()
d1 = arr[1] - arr[0]
d2 = arr[2] - arr[1]
max = max(d1, d2)
print(max - 1)