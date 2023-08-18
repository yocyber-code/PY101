l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("[", end="")
for i in range(len(l)):
    print(l[i], end="")
    if i != len(l) - 1:
        print(", ", end="")
print("]")
