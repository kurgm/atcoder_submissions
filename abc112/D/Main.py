#!/usr/bin/env python3
import sys


def solve(N: int, M: int):
    for d in reversed(range(1, M // N + 1)):
        if M % d == 0:
            print(d)
            return


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
