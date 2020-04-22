#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    print(max(len(set(S[:i]) & set(S[i:])) for i in range(1, N)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == '__main__':
    main()
