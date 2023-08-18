arr = []
while len(arr) < 10:
    arr.append(int(input()))
is_even = False
for i in arr :
    if i % 2 == 0:
        is_even = True
        break
if is_even:
    print("have")
else:
    print("don't have")