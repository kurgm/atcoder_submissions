#!/usr/bin/env python3
import collections
import sys
from typing import List

MOD = 998244353  # type: int


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def modinv(a):
    g, x, y = xgcd(a, MOD)
    return x % MOD


class BIT:
    def __init__(self, N: int):
        self.__N = 1 << (N - 1).bit_length()
        self.__arr = [0] * (self.__N + 1)

    def add(self, i: int, v: int):
        assert 0 <= i < self.__N
        j = i + 1
        dj = 1
        while j <= self.__N:
            self.__arr[j] += v
            while dj & j == 0:
                dj <<= 1
            j += dj

    def query(self, i: int) -> int:
        assert 0 <= i <= self.__N
        ans = 0
        j = i
        dj = 1
        while j != 0:
            ans += self.__arr[j]
            while dj & j == 0:
                dj <<= 1
            j -= dj
        return ans


def solve(N: int, A: "List[int]"):
    sA = sorted(A)
    iD: "dict[int, int]" = {}
    for i in range(N - 1, -1, -1):
        iD[sA[i]] = i
    Bc = BIT(N)
    Bs = BIT(N)
    dividend = 0
    for K1, Ai in enumerate(A):
        K = K1 + 1
        i = iD[Ai]
        iD[Ai] += 1
        Bc.add(i, 1)
        Bs.add(i, Ai)
        k = 1 + 2 * Bc.query(i)
        dividend += k * Ai
        dividend += 2 * (Bs.query(N) - Bs.query(i + 1))
        dividend %= MOD
        divisor = K * K % MOD
        print(dividend * modinv(divisor) % MOD)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
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