arr_2D = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
]


def print_arr():
    for i in range(len(arr_2D)):
        for j in range(len(arr_2D[i])):
            print(arr_2D[i][j], end='')
        print()


position = 0
while True:
    position = int(input())
    if position == -1:
        break
    direction = str(input())
    temp_arr = None
    if direction == 'u' or direction == 'd':
        temp_arr = []
        for i in range(len(arr_2D)):
            temp_arr.append(arr_2D[i][position])
        if direction == 'u':
            temp = temp_arr.pop(0)
            temp_arr.append(temp)
        else:
            temp = temp_arr.pop()
            temp_arr.insert(0, temp)
        for i in range(len(arr_2D)):
            arr_2D[i][position] = temp_arr[i]
        print_arr()
    if direction == 'l' or direction == 'r':
        temp_arr = arr_2D[position]
        if direction == 'l':
            temp = temp_arr.pop(0)
            temp_arr.append(temp)
        else:
            temp = temp_arr.pop()
            temp_arr.insert(0, temp)
        print_arr()
