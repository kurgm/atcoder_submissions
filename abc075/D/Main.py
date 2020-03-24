#!/usr/bin/env python3
from itertools import combinations
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, K: int, x: "List[int]", y: "List[int]"):
    pts = sorted(zip(x, y))
    ys = sorted(y)
    ans = float("inf")
    for y1, y2 in combinations(ys, 2):
        xs = [x for x, y in pts if y1 <= y <= y2]
        if len(xs) >= K:
            ans = min(
                ans,
                (y2 - y1) * min(x2 - x1 for x1, x2 in zip(xs, xs[K - 1:]))
            )
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, K, x, y)


if __name__ == '__main__':
    main()
