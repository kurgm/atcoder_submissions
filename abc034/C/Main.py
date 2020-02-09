#!/usr/bin/env python3
import sys


MOD = 1000000007  # type: int


def extgcd(a, b):
    # a * x + b * y = g
    if b == 0:
        return 1, 0, a
    q, r = divmod(a, b)
    y, x, g = extgcd(b, r)
    return x, y - q * x, g


def modinv(a, m=MOD):
    # a * x = 1 mod m
    # a * x - m * q = 1
    x, _iq, g = extgcd(a, m)
    assert g == 1
    return x


def solve(W: int, H: int):
    a = W + H - 2
    ans = 1
    for i in range(1, H):
        ans *= a + 1 - i
        ans %= MOD
        ans *= modinv(i)
        ans %= MOD
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    solve(W, H)


if __name__ == '__main__':
    main()
