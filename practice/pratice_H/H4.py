arr = []
while len(arr) < 10:
    arr.append(int(input()))
for i in arr:
    if i % 2 == 0:
        print(i)