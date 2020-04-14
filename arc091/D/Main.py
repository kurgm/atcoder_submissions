#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    print(sum(
        N // b * (b - K) + max(0, N % b - max(0, K - 1))
        for b in range(K + 1, N + 1)
    ))


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
