arr = []
while len(arr) < 3:
    arr.append(int(input()))
if arr[0] == arr[1] and arr[1] == arr[2]:
    print("a = b = c")
elif arr[0] == arr[1]:
    print("a = b")
elif arr[1] == arr[2]:
    print("b = c")
elif arr[0] == arr[2]:
    print("a = c")
else:
    print("a != b != c")
