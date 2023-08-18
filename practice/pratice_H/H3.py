arr = []
while len(arr) < 10:
    arr.append(int(input()))
for i in arr[-1::-1]:
    print(i)