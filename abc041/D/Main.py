#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, x: "List[int]", y: "List[int]"):
    dp = [0] * (1 << N)
    dp[0] = 1
    for i in range(1, 1 << N):
        ng = False
        for xi, yi in zip(x, y):
            if not (i & (1 << (xi - 1))) and (i & (1 << (yi - 1))):
                ng = True
                break
        if ng:
            continue
        t = 0
        for j in range(N):
            if i & (1 << j):
                t += dp[i & ~(1 << j)]
        dp[i] = t
    print(dp[(1 << N) - 1])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, x, y)


if __name__ == '__main__':
    main()
