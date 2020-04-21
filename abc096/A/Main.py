#!/usr/bin/env python3
import sys


def solve(a: int, b: int):
    print(a if a <= b else a - 1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(a, b)


if __name__ == '__main__':
    main()
