#!/usr/bin/env python3
import sys


def solve(n: int, m: int):
    print((n - 1) * (m - 1))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    solve(n, m)


if __name__ == '__main__':
    main()
