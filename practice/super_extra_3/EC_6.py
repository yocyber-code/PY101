arr = []
while len(arr) < 10:
    arr.append(int(input()))
arr.sort()
print(arr[-1::-1])