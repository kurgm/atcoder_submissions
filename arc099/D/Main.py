#!/usr/bin/env python3
from fractions import Fraction
import sys


def g():
    i = 1
    while True:
        si = str(i)
        ni = min({
            int(si[:j] + "9" * (len(si) - j))
            for j in range(len(si) + 1)
        }, key=lambda a: (Fraction(a, sum(int(x) for x in str(a))), a))
        yield ni
        i = ni + 1


def solve(K: int):
    it = g()
    for i in range(K):
        print(next(it))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)


if __name__ == '__main__':
    main()
