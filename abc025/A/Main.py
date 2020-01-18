#!/usr/bin/env python3

s = input()
n = int(input())

q, r = divmod(n - 1, 5)

print(s[q] + s[r])
