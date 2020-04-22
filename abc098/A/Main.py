#!/usr/bin/env python3
import sys


def solve(A: int, B: int):
    print(max(A + B, A - B, A * B))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == '__main__':
    main()
