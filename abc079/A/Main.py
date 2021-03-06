#!/usr/bin/env python3
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int):
    sN = str(N)
    print(YES if min(len(set(sN[:3])), len(set(sN[-3:]))) == 1 else NO)


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
