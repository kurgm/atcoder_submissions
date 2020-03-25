#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(R: int, G: int):
    print(2 * G - R)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    solve(R, G)


if __name__ == '__main__':
    main()
