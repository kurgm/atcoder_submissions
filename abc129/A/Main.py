#!/usr/bin/env python3
import sys


def solve(P: int, Q: int, R: int):
    print(P + Q + R - max(P, Q, R))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    P = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(P, Q, R)


if __name__ == '__main__':
    main()
