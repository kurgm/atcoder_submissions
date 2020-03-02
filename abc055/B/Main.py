#!/usr/bin/env python3
from functools import reduce
import sys

MOD = 1000000007  # type: int


def solve(N: int):
    print(reduce(lambda a, b: a * b % MOD, range(1, N + 1), 1))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
