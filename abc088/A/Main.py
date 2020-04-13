#!/usr/bin/env python3
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, A: int):
    print(YES if N % 500 <= A else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    solve(N, A)


if __name__ == '__main__':
    main()
