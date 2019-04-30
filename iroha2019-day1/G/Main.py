#!/usr/bin/env python3
import sys

n, m, k = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()] + [0]

dp = [[0] * (n + 2) for i in range(n + 2)]

for i in range(1, n + 2):
    dp[i][0] = -1
    for j in range(1, i + 1):
        p = max(
            dp[l][j - 1] for l in range(max(0, i - k), i)
        )
        if p != -1:
            p += a[i - 1]
        dp[i][j] = p

print(dp[n + 1][m + 1])
