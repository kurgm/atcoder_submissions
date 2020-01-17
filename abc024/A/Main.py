#!/usr/bin/env python3

a, b, c, k = [int(x) for x in input().split()]
s, t = [int(x) for x in input().split()]
if s + t >= k:
    a -= c
    b -= c

print(s * a + t * b)
