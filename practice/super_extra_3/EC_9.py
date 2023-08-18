import math


def polynomial(x, coefficients):
    result = 0
    for i, coef in enumerate(coefficients):
        result += coef * x ** (max_exponent - i)
    return result


def integral(a, b):
    num_segments = int((b - a) / ((b - a) / 1000))
    integral_sum = 0.5 * (polynomial(a, arr) + polynomial(b, arr))
    for i in range(1, num_segments):
        integral_sum += polynomial(a + i * ((b - a) / 1000), arr)
    return ((b - a) / 1000) * integral_sum


max_exponent = int(input())
arr = []
n = 0
while True:
    n = int(input())
    if n == -999:
        break
    arr.append(n)

a = float(input())
b = float(input())

integral_result = integral(a, b)
print(integral_result)
