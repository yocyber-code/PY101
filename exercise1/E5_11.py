a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)
print(x)
print(y)