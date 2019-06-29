#!/usr/bin/env python3
n = int(input())
p = [int(x) for x in input().split()]

ans = 0
for i in range(1, len(p) - 1):
    a, b, c = p[i - 1:i + 2]
    if a < b < c or a > b > c:
        ans += 1

print(ans)
