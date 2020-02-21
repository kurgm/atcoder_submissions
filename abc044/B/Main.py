#!/usr/bin/env python3
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(w: str):
    print(YES if all(
        w.count(chr(c)) % 2 == 0
        for c in range(ord("a"), ord("z") + 1)
    ) else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    w = next(tokens)  # type: str
    solve(w)


if __name__ == '__main__':
    main()
