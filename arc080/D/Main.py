#!/usr/bin/env python3
from itertools import chain, repeat
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(H: int, W: int, N: int, a: "List[int]"):
    it = chain.from_iterable(repeat(i + 1, ai) for i, ai in enumerate(a))
    for i in range(H):
        l = [next(it) for j in range(W)]
        if i % 2 == 1:
            l.reverse()
        print(*l)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(H, W, N, a)


if __name__ == '__main__':
    main()
