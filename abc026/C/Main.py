#!/usr/bin/env python3
from collections import defaultdict

n = int(input())

tr = defaultdict(set)
for i in range(1, n):
    bi = int(input()) - 1
    tr[bi].add(i)


def f(i):
    cs = [f(j) for j in tr[i]]
    if not cs:
        return 1
    return max(cs) + min(cs) + 1


print(f(0))
