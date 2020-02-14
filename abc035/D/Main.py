#!/usr/bin/env python3
from collections import defaultdict
import heapq
import sys
try:
    from typing import Dict, List, Tuple
except ImportError:
    pass


def sssp(g: "List[List[Tuple[int, int]]]") -> "List[int]":
    d = [0] + [float("inf")] * (len(g) - 1)
    q = [(di, i) for i, di in enumerate(d)]
    heapq.heapify(q)
    while q:
        di, vi = heapq.heappop(q)
        for vj, co in g[vi]:
            dj = di + co
            if dj < d[vj]:
                d[vj] = dj
                heapq.heappush(q, (dj, vj))
    return d


def solve(N: int, M: int, T: int, A: "List[int]", a: "List[int]", b: "List[int]", c: "List[int]"):
    g1 = [[] for _ in range(N)]  # type: List[List[Tuple[int, int]]]
    g2 = [[] for _ in range(N)]  # type: List[List[Tuple[int, int]]]
    for ai, bi, ci in zip(a, b, c):
        g1[ai - 1].append((bi - 1, ci))
        g2[bi - 1].append((ai - 1, ci))
    d1 = sssp(g1)
    d2 = sssp(g2)
    ans = 0
    for i in range(N):
        t = d1[i] + d2[i]
        if t > T:
            continue
        ans = max(ans, A[i] * (T - t))
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, T, A, a, b, c)


if __name__ == '__main__':
    main()
