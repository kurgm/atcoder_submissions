#!/usr/bin/env python3
from collections import Counter

n = int(input())
a = [int(x) for x in input().split()]

c = Counter(a)

ans = False
if len(c) == 1:
    ans = a[0] == 0
elif n % 3 == 0 and len(c) <= 3:
    nums = []
    for i in c:
        if c[i] % (n // 3) != 0:
            break
        else:
            nums += [i] * (c[i] // (n // 3))
    else:
        ans = (nums[0] ^ nums[1] ^ nums[2]) == 0

if ans:
    print("Yes")
else:
    print("No")
