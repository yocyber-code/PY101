def triangle(a, b, c):
    if a + b <= c:
        print('is not triangle')
        return
    elif a**2 + b**2 == c**2:
        print('right triangle')
    elif a ** 2 + b ** 2 > c ** 2:
        print('acute-angled triangle')
    else:
        print('obtuse triangle')
    if a == b and b == c:
        print('equilateral triangle')
    elif a == b or b == c or a == c:
        print('isosceles triangle')
    else:
        print('scalene triangle')


arr = []
while len(arr) < 3:
    arr.append(int(input()))
arr.sort()
triangle(arr[0], arr[1], arr[2])
