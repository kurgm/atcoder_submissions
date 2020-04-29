#!/usr/bin/env python3
import sys


def solve(K: int):
    print((K // 2) * ((K + 1) // 2))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)


if __name__ == '__main__':
    main()
