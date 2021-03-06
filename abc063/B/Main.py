#!/usr/bin/env python3
import sys


YES = "yes"  # type: str
NO = "no"  # type: str


def solve(S: str):
    print(YES if len(S) == len(set(S)) else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
