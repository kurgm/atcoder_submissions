#!/usr/bin/env python3
import sys


def solve(A: int, B: int):
    A -= 2
    A %= 13
    B -= 2
    B %= 13
    print("Alice" if A > B else "Bob" if B > A else "Draw")


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
