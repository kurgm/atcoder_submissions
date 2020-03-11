#!/usr/bin/env python3
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(x: int, y: int):
    a = [0, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]
    print(YES if a[x] == a[y] else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(x, y)


if __name__ == '__main__':
    main()
