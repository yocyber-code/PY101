arr = []
while len(arr) < 3:
    arr.append(int(input()))
a = arr[0] + arr[1]
b = arr[0] * arr[1]
c = arr[0] / arr[1]
d = arr[0] - arr[1]

if arr[2] == a:
    print("+")
elif arr[2] == b:
    print("*")
elif arr[2] == c:
    print("/")
elif arr[2] == d:
    print("-")
