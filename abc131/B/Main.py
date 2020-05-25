#!/usr/bin/env python3
import sys


def solve(N: int, L: int):
    ls = range(L, L + N)
    print(sum(ls) - min(ls, key=abs))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    solve(N, L)


if __name__ == '__main__':
    main()
