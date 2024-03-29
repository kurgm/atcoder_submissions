#!/usr/bin/env python3
import collections
import sys
from typing import List


def solve(N: int, M: int, K: int, u: "List[int]", v: "List[int]", a: "List[int]", s: "List[int]"):
    g: "dict[int, list[int]]" = collections.defaultdict(list)
    for ui, vi, ai in zip(u, v, a):
        if ai == 1:
            g[ui].append(vi)
            g[vi].append(ui)
        else:
            g[-ui].append(-vi)
            g[-vi].append(-ui)

    ss = set(s)
    res = {1: 0}
    if 1 == N:
        print(0)
        return
    if 1 in ss:
        res[-1] = 0
    q = collections.deque(res.keys())
    while q:
        p_0 = q.popleft()
        cost = res[p_0] + 1
        for p_1 in g.get(p_0, []):
            if abs(p_1) == N:
                print(cost)
                return
            if p_1 not in res:
                res[p_1] = cost
                q.append(p_1)
            if abs(p_1) in ss and -p_1 not in res:
                res[-p_1] = cost
                q.append(-p_1)

    print(-1)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    a = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
        a[i] = int(next(tokens))
    s = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, M, K, u, v, a, s)


if __name__ == '__main__':
    main()
