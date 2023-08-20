a = int(input())
b = int(input())
c = int(input())

if a > 13:
    if b != 6:
        print("A")
    elif c <= 7:
        print("B")
    else:
        print("C")
elif b <= 16:
    print("D")
elif c > 6:
    print("E")
else:
    print("F")
