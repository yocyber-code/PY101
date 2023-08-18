arr = []
g = 6.67 * 10**-11
while len(arr) < 3:
    arr.append(float(input()))
f = (g*arr[0]*arr[1])/arr[2]**2
print(f)