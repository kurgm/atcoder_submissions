#!/usr/bin/env python3
from itertools import combinations

print(sorted(
    set(map(sum, combinations(map(int, input().split()), 3))),
    reverse=True)[2])
