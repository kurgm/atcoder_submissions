#!/usr/bin/env python3
import sys


def solve(N: int, M: int):
    print((M * 1900 + (N - M) * 100) * 2 ** M)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)


if __name__ == '__main__':
    main()
