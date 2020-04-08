#!/usr/bin/env python3
import re
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: int, B: int, S: str):
    print(YES if re.match(r"\d" * A + "-" + r"\d" * B, S) else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(A, B, S)


if __name__ == '__main__':
    main()
