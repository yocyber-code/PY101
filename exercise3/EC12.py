arr = []
while len(arr) < 5:
    arr.append(int(input()))
a = arr[1:]
a.append(arr[0])
print(a)
