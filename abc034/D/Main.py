#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, K: int, w: "List[int]", p: "List[int]"):
    def is_ok(pj):
        return sum(sorted(
            (pi - pj) * wi for wi, pi in zip(w, p)
        )[-K:]) > 0
    lb = 0.0
    hb = 100.0
    while hb - lb > 1e-12:
        m = (lb + hb) / 2.0
        if is_ok(m):
            lb = m
        else:
            hb = m
    print(lb)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    p = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        p[i] = int(next(tokens))
    solve(N, K, w, p)


if __name__ == '__main__':
    main()
