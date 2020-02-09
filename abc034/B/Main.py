#!/usr/bin/env python3
import sys


def solve(n: int):
    print(n + (1 if n % 2 == 1 else -1))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    solve(n)


if __name__ == '__main__':
    main()
