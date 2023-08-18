w_a = float(input())
p_a = float(input())
w_b = float(input())
p_b = float(input())

u_a = p_a / w_a
u_b = p_b / w_b

if u_a > u_b:
    print("B is cheaper than A")
elif u_a < u_b:
    print("A is cheaper than B")
else:
    print("Equal price")