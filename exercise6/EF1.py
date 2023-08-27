arr = []
while len(arr) < 4:
    arr.append(int(input()))
arr.sort()
print(float(sum(arr)))
print(float(sum(arr[1:])))
