#!/usr/bin/env python3
import sys


def solve(N: int):
    a = 2
    b = 1
    for i in range(N - 1):
        a, b = b, a + b
    print(b)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
