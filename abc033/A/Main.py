#!/usr/bin/env python3
import sys


def solve(N: int):
    if N % 1111 == 0:
        print("SAME")
    else:
        print("DIFFERENT")


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
