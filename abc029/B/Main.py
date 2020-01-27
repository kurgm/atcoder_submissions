#!/usr/bin/env python3
from collections import Counter
print(sum(Counter(set(input()))["r"] for _ in range(12)))
