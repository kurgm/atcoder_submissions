#!/usr/bin/env python3
import sys


def solve(a: str, b: str):
    print("HD"[(a == "H") ^ (b == "H")])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = next(tokens)  # type: str
    b = next(tokens)  # type: str
    solve(a, b)


if __name__ == '__main__':
    main()
