#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(L: int, H: int, N: int, A: "List[int]"):
    for ai in A:
        print(-1 if ai > H else max(0, L - ai))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(L, H, N, A)


if __name__ == '__main__':
    main()
