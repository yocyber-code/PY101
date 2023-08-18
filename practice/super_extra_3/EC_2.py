arr = []
while len(arr) < 10:
    arr.append(int(input()))
v = int(input())
isFound = False
for i in arr:
    if i == v:
        isFound = True
        break
if isFound:
    print("V is in array")
else:
    print("is not in array")
