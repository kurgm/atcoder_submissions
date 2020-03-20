#!/usr/bin/env python3
import sys


def solve(X: int, t: int):
    print(max(X - t, 0))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    t = int(next(tokens))  # type: int
    solve(X, t)


if __name__ == '__main__':
    main()
