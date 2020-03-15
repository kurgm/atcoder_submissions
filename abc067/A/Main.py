#!/usr/bin/env python3
import sys


YES = "Possible"  # type: str
NO = "Impossible"  # type: str


def solve(A: int, B: int):
    print(YES if A * B * (A + B) % 3 == 0 else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == '__main__':
    main()
