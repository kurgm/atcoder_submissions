#!/usr/bin/env python3

n, t = [int(x) for x in input().split()]

ans = 0
d_o = int(input())
d_w_c = d_o + t

for i in range(n - 1):
    ai = int(input())
    if ai < d_w_c:
        d_w_c = ai + t
    else:
        ans += d_w_c - d_o
        d_o = ai
        d_w_c = d_o + t

ans += d_w_c - d_o

print(ans)
