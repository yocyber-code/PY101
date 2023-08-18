import sys
count = 0
for i in range(1, 111):
    if i % 3 == 0:
        sys.stdout.write("Coza")
    if i % 5 == 0:
        sys.stdout.write("Loza")
    if i % 7 == 0:
        sys.stdout.write("Woza")
    if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        sys.stdout.write(str(i))
    count += 1
    if count % 11 == 0:
        print()
