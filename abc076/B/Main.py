#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    ans = 1
    for _ in range(N):
        ans = min(ans * 2, ans + K)
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
