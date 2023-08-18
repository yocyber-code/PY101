arr = []
while len(arr) < 10:
    arr.append(int(input()))
v = int(input())
for i in range(len(arr)):
    if arr[i] == v:
        arr.pop(i)
        arr.append(0)
print(arr)