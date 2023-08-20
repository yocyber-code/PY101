n = int(input())
arr = []
while len(arr) < n:
    arr.append(int(input()))
print(min(arr))
print(max(arr))
print(sum(arr) / len(arr))
