#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

import itertools


def solve(N: int, S: "List[str]", P: "List[int]"):
    s = sum(P)
    print(next(itertools.chain(
        (si for si, pi in zip(S, P) if pi * 2 > s),
        ["atcoder"]
    )))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [str()] * (N)  # type: "List[str]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = next(tokens)
        P[i] = int(next(tokens))
    solve(N, S, P)


if __name__ == '__main__':
    main()
