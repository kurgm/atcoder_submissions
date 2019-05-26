#!/usr/bin/env python3

from itertools import product

n, m = [int(x) for x in input().split()]
s = [[int(x) - 1 for x in input().split()][1:] for i in range(m)]
p = [int(x) for x in input().split()]

ans = 0

for ss in product((0, 1), repeat=n):
    for st, par in zip(s, p):
        if (sum(ss[sti] for sti in st) & 1) != par:
            break
    else:
        ans += 1

print(ans)
