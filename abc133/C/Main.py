#!/usr/bin/env python3
from itertools import combinations

l, r = [int(x) for x in input().split()]

if r - l >= 2019:
    l = r = 0

l %= 2019
r %= 2019
if l >= r:
    r += 2019

ans = min(i * j % 2019 for i, j in combinations(range(l, r + 1), 2))
print(ans)
