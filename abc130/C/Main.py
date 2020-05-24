#!/usr/bin/env python3
import sys


def solve(W: int, H: int, x: int, y: int):
    print(W * H / 2, 1 if (2 * x, 2 * y) == (W, H) else 0)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(W, H, x, y)


if __name__ == '__main__':
    main()
