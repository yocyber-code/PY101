current = -1
total = 0
count = 0
while current != 0:
    current = int(input())
    if current == 0:
        break
    if current < 0:
        print("ERROR")
    else:
        total += current
        count += 1
if(count == 0):
    print("NO AVERAGE")
else:
    print(total/count)