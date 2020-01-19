#!/usr/bin/env python3
import math
n = int(input())
r = [int(input()) for _ in range(n)]
r.sort(reverse=True)
s = sum((-1) ** i * ri ** 2 for i, ri in enumerate(r))
print(math.pi * s)
