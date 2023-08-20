a = int(input())
b = int(input())
c = int(input())
d = int(input())

q = b * d
a = q / b * a
c = q / d * c
p = int(a + c)
print(p, q, sep='/')
for i in range(min(p, q) - 1, 1, -1):
    if p % i == 0 and q % i == 0:
        p = p / i
        q = q / i
print(int(p), int(q), sep='/')
