arr = []
while len(arr) < 10:
    arr.append(int(input()))
arr.sort()
max = 0
counter = 1
number = 0
for i in range(1, len(arr)):
    if (arr[i] == arr[i-1]):
        counter += 1
        if (counter > max):
            max = counter
            number = arr[i-1]
    else:
        counter = 1
print(number)
print(max)
