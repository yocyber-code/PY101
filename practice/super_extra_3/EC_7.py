arr_a = []
while len(arr_a) < 10:
    arr_a.append(int(input()))
arr_b = []
while len(arr_b) < 10:
    arr_b.append(int(input()))
arr_c = arr_a.copy()
arr_c.extend(arr_b)
print(arr_c)