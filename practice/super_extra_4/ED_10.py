employee_hour = []
while len(employee_hour) < 5:
    hour = []
    while len(hour) < 7:
        hour.append(int(input()))
    employee_hour.append(sum(hour))
for i in employee_hour:
    print(i)
