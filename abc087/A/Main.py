#!/usr/bin/env python3
import sys


def solve(X: int, A: int, B: int):
    print((X - A) % B)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(X, A, B)


if __name__ == '__main__':
    main()
