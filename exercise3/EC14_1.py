n = str(input())
n = n.split('e')
n = float(n[0]) * 10**float(n[1])
Euler = (1 + 1 / n)**n
print(Euler)
