#!/usr/bin/env python3

n, a, b = [int(x) for x in input().split()]

pos = 0

for _ in range(n):
    s, d_ = input().split()
    d = int(d_)
    if d < a:
        d = a
    elif d > b:
        d = b
    if s == "East":
        pos += d
    else:
        pos -= d

if pos == 0:
    print("0")
else:
    print(("East" if pos > 0 else "West"), abs(pos))
