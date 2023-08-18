max = None
for i in range(0, 2):
    in1 = int(input())
    if (max == None or max < in1):
        max = in1
print(max)
