#!/usr/bin/env python3
import sys

from fractions import gcd

MOD = 1000000007  # type: int


def solve(N: int, A: "List[int]"):
    s = 0
    m = 1
    for i, Ai in enumerate(A):
        g = gcd(m, Ai)
        Ai_g = Ai // g
        s = s * Ai_g % MOD
        m *= Ai_g
        s = (s + (m // Ai) % MOD) % MOD
    print(s)


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
