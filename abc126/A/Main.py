#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, K: int, S: str):
    print(S[:K - 1] + S[K - 1].lower() + S[K:])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, S)


if __name__ == '__main__':
    main()
