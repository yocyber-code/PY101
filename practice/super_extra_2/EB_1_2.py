total = int(input())
arr = []
while len(arr) < total:
    arr.append(int(input()))
print(sum(arr)/total)
print(min(arr))
print(max(arr))