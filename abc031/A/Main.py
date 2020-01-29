#!/usr/bin/env python3
a, d = [int(x) for x in input().split()]
print(max((a + 1) * d, a * (d + 1)))
