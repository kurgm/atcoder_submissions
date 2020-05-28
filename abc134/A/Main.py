#!/usr/bin/env python3
import sys


def solve(r: int):
    print(3 * r * r)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    r = int(next(tokens))  # type: int
    solve(r)


if __name__ == '__main__':
    main()
