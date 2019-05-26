#!/usr/bin/env python3
n, k = [int(_) for _ in input().split()]
v = [int(_) for _ in input().split()]

ans = 0

for l in range(n):
    for r in range(n - l + 1):
        if l + r > k:
            break
        nv = v[:l] + v[n - r:]
        nv.sort()
        for i in range(k - l - r):
            if not nv or nv[0] >= 0:
                break
            del nv[0]
        ans = max(ans, sum(nv))

print(ans)
