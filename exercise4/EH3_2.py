n = int(input())
n = str(n)
odd = 0
even = 0
for i in n:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, odd, sep='\n')
