n = int(input())
if n > 0 and n <= 3:
    x = float(input())
    y = float(input())
    match n:
        case 1:
            print(x + y)
        case 2:
            print(x * y)
        case 3:
            print(x / y)
else:
    print("please select only 1-3")
