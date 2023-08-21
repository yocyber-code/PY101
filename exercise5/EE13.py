n = int(input())
arr = []
while len(arr) < n:
    score = []
    while len(score) < 5:
        score.append(int(input()))
    arr.append(score.copy())

for i in range(len(arr)):
    print(float(sum(arr[i])) / 5)
for i in range(5):
    sum = 0
    for j in range(len(arr)):
        sum += arr[j][i]
    print(float(sum) / len(arr))
