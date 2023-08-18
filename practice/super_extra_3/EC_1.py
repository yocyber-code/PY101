arr = []
count = 0
while len(arr) < 10:
    arr.append(int(input()))

for i in arr:
    if i >= 10:
        count += 1
print(count)
