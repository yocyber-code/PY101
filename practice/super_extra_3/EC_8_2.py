arr_1_len = int(input())
arr1 = []
while len(arr1) < arr_1_len:
    arr1.append(int(input()))

arr_2_len = int(input())
arr2 = []
while len(arr2) < arr_2_len:
    arr2.append(int(input()))

convolution = []
for i in range(len(arr1) - len(arr2) + 1):
    convolution.append(0)
    for j in range(len(arr2)):
        convolution[i] += arr1[i + j] * arr2[j]
print(convolution)
