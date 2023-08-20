arr = []
while True:
    n = int(input())
    if n == 0:
        break
    arr.append(n)
print(sum(arr))
print(sum(arr) / len(arr))
