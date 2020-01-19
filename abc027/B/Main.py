#!/usr/bin/env python3
n = int(input())
a = [int(x) for x in input().split()]
q, r = divmod(sum(a), n)
if r != 0:
    print(-1)
else:
    cs = 0
    ans = 0
    for i, ai in enumerate(a):
        if cs != q * i:
            ans += 1
        cs += ai
    print(ans)
