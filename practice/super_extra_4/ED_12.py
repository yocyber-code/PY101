
patterns = [
    ["xxxx", "x--x", "x--x", "x--x", "xxxx"],
    ["---x", "---x", "---x", "---x", "---x"],
    ["xxxx", "---x", "xxxx", "x---", "xxxx"],
    ["xxxx", "---x", "xxxx", "---x", "xxxx"],
    ["x--x", "x--x", "xxxx", "---x", "---x"],
    ["xxxx", "x---", "xxxx", "---x", "xxxx"],
    ["x---", "x---", "xxxx", "x--x", "xxxx"],
    ["xxxx", "---x", "---x", "---x", "---x"],
    ["xxxx", "x--x", "xxxx", "x--x", "xxxx"],
    ["xxxx", "x--x", "xxxx", "---x", "---x"]
]

n = str(input())
for i in range(5):
    for j in range(len(n)):
        print(patterns[int(n[j])][i], end="")
        if j != len(n) - 1:
            print("\t", end="")
    print()
