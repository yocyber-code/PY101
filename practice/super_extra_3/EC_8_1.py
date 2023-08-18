arr1 = [1, 2, 1, 3, 8, 5, 4, 6, 8, 4, 2, 5, 6, 1, 2, 1, 0, 0, 1, 0]
arr2 = [-1, 0, 1]
convolution = []
for i in range(len(arr1) - len(arr2) + 1):
    convolution.append(0)
    for j in range(len(arr2)):
        convolution[i] += arr1[i + j] * arr2[j]
print(convolution)