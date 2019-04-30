#!/usr/bin/env python3
n, x, y = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

a.sort(reverse=True)

x += sum(a[0::2])
y += sum(a[1::2])

if x == y:
    print("Draw")
elif x > y:
    print("Takahashi")
else:
    print("Aoki")
