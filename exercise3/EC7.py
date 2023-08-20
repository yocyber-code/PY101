n = int(input())
str = str(n)
for i in range(len(str)-1, -1, -1):
    print(str[i], end="")
