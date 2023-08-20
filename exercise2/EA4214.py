arr = []
while len(arr) < 3:
    arr.append(int(input()))
arr.sort()
if arr[0] + arr[1] <= arr[2]:
    print("not triangle")
else:
    print("triangle")
