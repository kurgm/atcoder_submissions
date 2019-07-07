#!/usr/bin/env python3
n = int(input())
a = [int(x) for x in input().split()]

v = sum(a[i] * (-1) ** (i % 2) for i in range(n))

ans = [0] * n

for i in range(n):
    ans[i] = v
    v = -v + 2 * a[i]

print(" ".join(str(x) for x in ans))
