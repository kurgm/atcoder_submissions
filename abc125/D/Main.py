#!/usr/bin/env python3

n = int(input())
a = [int(x) for x in input().split()]

nns = len([x for x in a if x < 0])

ans = sum(abs(x) for x in a)
if nns % 2 != 0:
    m = min(abs(x) for x in a)
    ans -= m * 2

print(ans)
