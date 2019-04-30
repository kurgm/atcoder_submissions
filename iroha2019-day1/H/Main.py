#!/usr/bin/env python3

n = int(input())
f = sum(int(x) for x in str(n))

q, r = divmod(f, 9)
x = int(str(r) + "9" * q)

if n != x:
    print(x)
elif q:
    print(str(r + 1) + "8" + "9" * (q - 1))
else:
    print(r + 9)

