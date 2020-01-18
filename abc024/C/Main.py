#!/usr/bin/env python3

n, d, k = [int(x) for x in input().split()]
lrs = [[int(x) for x in input().split()] for _ in range(d)]
for _ in range(k):
    s, t = [int(x) for x in input().split()]
    if s < t:
        for i, (l, r) in enumerate(lrs):
            if l <= s <= r:
                s = r
                if s >= t:
                    print(i + 1)
                    break
        else:
            assert False
    else:
        for i, (l, r) in enumerate(lrs):
            if l <= s <= r:
                s = l
                if s <= t:
                    print(i + 1)
                    break
        else:
            assert False
