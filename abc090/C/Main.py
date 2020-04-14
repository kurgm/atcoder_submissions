#!/usr/bin/env python3
import sys


def solve(N: int, M: int):
    print(abs(N - 2) * abs(M - 2))


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
