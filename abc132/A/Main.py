#!/usr/bin/env python3
s = input()

ans = True
if len(set(s)) != 2:
    ans = False
else:
    a, b = list(set(s))
    if s.count(a) == s.count(b) == 2:
        pass
    else:
        ans = False

print("Yes" if ans else "No")
