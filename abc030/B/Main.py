#!/usr/bin/env python3
n, m = [int(x) for x in input().split()]

h1 = n * 30 + m * 0.5
h2 = m * 6
d = (h1 - h2) % 360

print(min(d, 360 - d))
