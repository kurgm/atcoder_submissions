#!/usr/bin/env python3
from functools import reduce
import sys
try:
    from typing import List, Tuple
except ImportError:
    pass

MOD = 1000000007  # type: int


def dfs(g: "List[List[int]]", node: int, parent: int) -> "Tuple[int, int]":
    chs = [dfs(g, i, node) for i in g[node] if i != parent]
    nb = reduce(lambda acc, bw: acc * bw[1] % MOD, chs, 1)
    nw = reduce(lambda acc, bw: acc * (bw[0] + bw[1]) % MOD, chs, 1)
    return nb, nw


def solve(N: int, a: "List[int]", b: "List[int]"):
    g = [[] for _ in range(N)]  # type: List[List[int]]
    for ai, bi in zip(a, b):
        g[ai - 1].append(bi - 1)
        g[bi - 1].append(ai - 1)
    nb, nw = dfs(g, 0, -1)
    print((nb + nw) % MOD)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)


if __name__ == '__main__':
    main()
