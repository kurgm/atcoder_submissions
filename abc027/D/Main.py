#!/usr/bin/env python3
s = input()

ms = []
cs = 0
for c in s:
    if c == "+":
        cs += 1
    elif c == "-":
        cs -= 1
    else:
        ms.append(cs)

ms.sort()
lm = len(ms) // 2
print(sum(ms[lm:]) - sum(ms[:lm]))
