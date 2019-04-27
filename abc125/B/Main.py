#!/usr/bin/env python3

n = int(input())
v = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

ans = sum(max(x - y, 0) for x, y in zip(v, c))

print(ans)
