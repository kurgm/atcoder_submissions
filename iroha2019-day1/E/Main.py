#!/usr/bin/env python3
n, a, b = [int(_) for _ in input().split()]
if b == 0:
    d = []
else:
    d = [int(_) for _ in input().split()]

d.sort()
dj = 0
nd = 0
for di in d + [n + 1]:
    q, r = divmod(di - dj, a)
    if r == 0:
        nd += q
    else:
        nd += q + 1
    dj = di

print(n - (nd - 1))
