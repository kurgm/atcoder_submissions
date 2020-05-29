#!/usr/bin/env python3
import sys


def solve(N: int, D: int):
    print(-(-N // (2 * D + 1)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(N, D)


if __name__ == '__main__':
    main()
