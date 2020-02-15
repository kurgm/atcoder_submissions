#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, w: "List[int]", h: "List[int]"):
    whs = sorted(zip(w, h), key=lambda a: (a[0], -a[1]))
    dp = [float("inf")] * (N + 1)
    dp[0] = 0
    ans = 0
    for _wi, hi in whs:
        lb = 0
        hb = len(dp)
        while hb - lb > 1:
            m = (lb + hb) // 2
            if dp[m] < hi:
                lb = m
            else:
                hb = m
        dp[lb + 1] = hi
        ans = max(ans, lb + 1)

    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    h = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        h[i] = int(next(tokens))
    solve(N, w, h)


if __name__ == '__main__':
    main()
