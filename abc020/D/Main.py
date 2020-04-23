#!/usr/bin/env python3
from functools import reduce
from itertools import product
import sys


MOD = 1000000007  # type: int


def fb(n: int):
    if n % 2 == 0:
        cnt = 0
        while n % 2 == 0:
            cnt += 1
            n //= 2
        yield 2, cnt
    i = 3
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            yield i, cnt
        i += 2
    if n != 1:
        yield n, 1


def solve(N: int, K: int):
    ans = 0
    for dfactors in product(*(
            [b ** r for r in range(cnt + 1)] for b, cnt in fb(K))):
        d = reduce(lambda a, b: a * b, dfactors, 1)
        n = N // d
        k = K // d
        ans1 = 0
        for factors in product(*((1, b) for b, _cnt in fb(k))):
            factors = [f for f in factors if f != 1]
            v = reduce(lambda a, b: a * b, factors, 1)
            cnt = n // v
            ans1 += (-1) ** len(factors) * v * cnt * (cnt + 1) // 2
            ans1 %= MOD
        ans += ans1 * k * d
        ans %= MOD
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    main()
