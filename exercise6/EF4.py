def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


d = int(input())
m = int(input())
y = int(input()) - 543
arr_days = [31, 28 + is_leap_year(y), 31,
            30, 31, 30, 31, 31, 30, 31, 30, 31]

is_leap = is_leap_year(y)
for i in range(0, m - 1):
    d += arr_days[i]
print(d)
