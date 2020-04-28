#!/usr/bin/env python3
import sys


def solve(N: int, i: int):
    print(N - i + 1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    i = int(next(tokens))  # type: int
    solve(N, i)


if __name__ == '__main__':
    main()
