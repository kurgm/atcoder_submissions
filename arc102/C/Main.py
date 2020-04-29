#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    if K % 2 == 0:
        k2 = K // 2
        print(((N // k2 + 1) // 2) ** 3 + (N // K) ** 3)
    else:
        print((N // K) ** 3)


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
