h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
if h1 > h2:
    h2 += 12
elif h1 == h2:
    if m1 > m2:
        h2 += 12
    elif m1 == m2:
        h2 += 24
if m1 > m2:
    m2 += 60
    h2 -= 1
print(h2 - h1, m2 - m1, sep='\n')
