#!/usr/bin/env python3
import sys


def solve(S: int, K: int):
    K -= 1
    for c in str(S):
        if c == "1":
            K -= 1
        else:
            K = -1
        if K < 0:
            print(c)
            return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(S, K)


if __name__ == '__main__':
    main()
