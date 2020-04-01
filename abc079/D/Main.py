#!/usr/bin/env python3
from collections import Counter
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(H: int, W: int, c: "List[List[int]]", A: "List[List[int]]"):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])

    ctr = Counter(Aij for Ai in A for Aij in Ai)
    print(sum(ctr[n] * c[n][1] for n in range(10)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    c = [[int(next(tokens)) for _ in range(9 - 0 + 1)] for _ in range(9 - 0 + 1)]  # type: "List[List[int]]"
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, c, A)


if __name__ == '__main__':
    main()
