#!/usr/bin/env python3
from itertools import combinations

n, d = [int(x) for x in input().split()]
xs = [[int(x) for x in input().split()] for _ in range(n)]

def p(a, b):
    d2 = sum((ai - bi) ** 2 for ai, bi in zip(a, b))
    return int(d2 ** 0.5) ** 2 == d2

ans = 0
for a, b in combinations(xs, 2):
    if p(a, b):
        ans += 1

print(ans)
