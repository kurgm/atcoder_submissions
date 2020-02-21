#!/usr/bin/env python3
import sys


def solve(N: int, K: int, X: int, Y: int):
    print(X * min(N, K) + Y * max(0, N - K))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(N, K, X, Y)


if __name__ == '__main__':
    main()
