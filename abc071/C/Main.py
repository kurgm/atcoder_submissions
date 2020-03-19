#!/usr/bin/env python3
from collections import Counter
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, A: "List[int]"):
    def g():
        ctr = Counter(A)
        for key in sorted(ctr.keys(), reverse=True):
            for _ in range(ctr[key] // 2):
                yield key
    gg = g()
    try:
        print(next(gg) * next(gg))
    except StopIteration:
        print(0)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
