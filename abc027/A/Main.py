#!/usr/bin/env python3
l1, l2, l3 = sorted(int(x) for x in input().split())
print(l3 if l1 == l2 else l1)
