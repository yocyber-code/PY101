arr_pos = []
arr_neg = []
while True:
    n = int(input())
    if n == 0:
        break
    if n > 0:
        arr_pos.append(n)
    else:
        arr_neg.append(n)
print(sum(arr_pos))
print(sum(arr_neg))
