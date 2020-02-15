#!/usr/bin/env python3
import sys


YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(S: str):
    print(YES if S[-1] == "T" else NO)


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
