#!/usr/bin/env python3
import sys


def solve(M: int):
    print(48 - M)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    M = int(next(tokens))  # type: int
    solve(M)


if __name__ == '__main__':
    main()
