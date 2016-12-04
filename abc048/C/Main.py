# -*- coding: utf-8 -*-

n, x = [int(w) for w in raw_input().split()]
a = [int(w) for w in raw_input().split()]

b = [a[i] + a[i+1] for i in xrange(n - 1)]

ans = 0
for i in xrange(n - 1):
    if b[i] > x:
        d = b[i] - x
        ans += d
        b[i] = x
        if i < n - 2:
            b[i + 1] = b[i + 1] - min(d, a[i + 1])

print ans
