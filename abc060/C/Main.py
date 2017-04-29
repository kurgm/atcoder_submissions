n, T = [int(_) for _ in raw_input().split()]
s = 0
S = 0
x = 0
for t in [int(_) for _ in raw_input().split()]:
    e = s + T
    if e < t:
        x += e - S
        S = t
    s = t

x += t + T - S

print(x)