#!/usr/bin/env python3

n = int(input())
r = 1
ans = 0
while 1:
    b, c = divmod(n, r)
    if b == 0:
        break
    a, b = divmod(b, 10)
    ans += a * r
    if b > 1:
        ans += r
    elif b == 1:
        ans += c + 1
    r *= 10
print(ans)
