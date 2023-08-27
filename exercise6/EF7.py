n = str(input())
sum = 0
for i in range(0, len(n)):
    sum += (i + 1) * int(n[i])
sum = sum % 11
print(n + str(sum))
