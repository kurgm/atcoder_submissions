#!/usr/bin/env python3
s = input()
k = int(input())
k %= len(s)
print(s[k:] + s[:k])
