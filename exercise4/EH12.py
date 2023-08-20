arr_even = []
arr_odd = []
for i in range(10):
    n = int(input())
    if n % 2 == 0:
        arr_even.append(n)
    else:
        arr_odd.append(n)

if (len(arr_odd) == 0):
    print(0)
    print(0)
else:
    print(max(arr_odd))
    print(min(arr_odd))

if (len(arr_even) == 0):
    print(0)
    print(0)
else:
    print(max(arr_even))
    print(min(arr_even))
