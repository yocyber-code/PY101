import sys
sys.stdout.write("*|")
for i in range(1, 10):
    sys.stdout.write("\t"+str(i))
print()
for i in range(0, 77):
    sys.stdout.write("-")
print()

for i in range(1, 10):
    sys.stdout.write(str(i)+"|")
    for j in range(1, 10):
        sys.stdout.write("\t"+str(i*j))
    print()
