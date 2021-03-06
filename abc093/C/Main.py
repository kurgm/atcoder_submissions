#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int):
    x = 3 * max([A, B, C]) - A - B - C
    print(x // 2 + x % 2 * 2)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)


if __name__ == '__main__':
    main()
