m = int(input())
percent = int(input())
balance = 0
for i in range(1, 11):
    balance += m
    balance += balance * (percent / 100)
print(balance)
