#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    b = N * N * N
    a = 1
    a += 3 * (N - 1)
    a += 6 * (K - 1) * (N - K)
    print(a / b)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
