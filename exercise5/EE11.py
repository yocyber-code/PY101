n = int(input())
arr = []
while len(arr) < n:
    arr.append(int(input()))
print(float(max(arr)))
print(float(min(arr)))
print(float(sum(arr)) / n)
