#!/usr/bin/env python3
import sys


def solve(X: int):
    print(X // 500 * 1000 + X % 500 // 5 * 5)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)


if __name__ == '__main__':
    main()
