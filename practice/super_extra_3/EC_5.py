arr = []
while len(arr) < 10:
    arr.append(int(input()))
v = int(input())
index = int(input())
arr.insert(index, v)
arr.pop(len(arr) - 1)
print(arr)