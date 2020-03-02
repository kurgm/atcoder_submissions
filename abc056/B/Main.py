#!/usr/bin/env python3
import sys


def solve(W: int, a: int, b: int):
    print(max(0, abs(a - b) - W))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(W, a, b)


if __name__ == '__main__':
    main()
