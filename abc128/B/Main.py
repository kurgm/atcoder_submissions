#!/usr/bin/env python3
n = int(input())
res = [[i] + input().split() for i in range(n)]

res.sort(key=lambda x: (x[1], -int(x[2])))

for r in res:
    print(r[0] + 1)
