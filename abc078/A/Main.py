#!/usr/bin/env python3
import sys


def solve(X: str, Y: str):
    print("<" if X < Y else ">" if X > Y else "=")


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = next(tokens)  # type: str
    Y = next(tokens)  # type: str
    solve(X, Y)


if __name__ == '__main__':
    main()
