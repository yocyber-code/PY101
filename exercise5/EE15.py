def cal_pascals(n):
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)
    return triangle


n = int(input())
pascal_arr = cal_pascals(n)
for i in range(len(pascal_arr)):
    for j in range(len(pascal_arr) - i, 1, -1):
        print(end='\t')
    for j in range(len(pascal_arr[i])):
        if j == len(pascal_arr[i]) - 1:
            print(pascal_arr[i][j])
        else:
            print(pascal_arr[i][j], end='\t\t')
