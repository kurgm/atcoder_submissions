#!/usr/bin/env python3
from collections import Counter
import math
import sys
try:
    import typing
    from typing import List, Tuple
except ImportError:
    pass

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]", B: "List[int]"):
    nz = 0
    c = Counter()  # type: typing.Counter[Tuple[int, int]]
    for Ai, Bi in zip(A, B):
        if Ai == Bi == 0:
            nz += 1
            continue
        g = math.gcd(Ai, Bi)
        Ai //= g
        Bi //= g
        if Ai == 0 and Bi < 0 or Ai < 0:
            Ai *= -1
            Bi *= -1
        c[Ai, Bi] += 1
    dc = dict(c)
    ans = 1
    for Ai, Bi in dc:
        na = dc[Ai, Bi]
        if Bi <= 0:
            if (-Bi, Ai) in dc:
                nb = dc[-Bi, Ai]
                ans = ans * (pow(2, na, MOD) + pow(2, nb, MOD) - 1) % MOD
            else:
                ans = ans * pow(2, na, MOD) % MOD
        else:
            if (Bi, -Ai) not in dc:
                ans = ans * pow(2, na, MOD) % MOD
    ans -= 1
    ans += nz
    ans %= MOD
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)


if __name__ == '__main__':
    main()
