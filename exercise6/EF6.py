n = str(input())
n = '978' + str(n[0:len(n)-1])
sum = 0
for i in range(0, len(n)):
    if i % 2 == 0:
        sum += int(n[i])
    else:
        sum += int(n[i]) * 3
sum = sum % 10
if sum != 0:
    sum = 10 - sum
print(n + str(sum))
