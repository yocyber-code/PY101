arr = [0, 0, 0, 0]
n = int(input())
n = str(n)
for i in range(len(n)):
    arr.pop()
for i in range(len(n)):
    arr.append(int(n[i]))
print(arr)
