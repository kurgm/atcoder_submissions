#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    ans = 0.0
    if N >= K:
        ans += (N - K + 1) / N
    k = K
    p = 1.0
    while k > 1:
        j = -(-k // 2)
        p /= 2.0
        ans += (min(k, N + 1) - min(j, N + 1)) / N * p
        k = j
    print(ans)


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
