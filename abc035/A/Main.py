#!/usr/bin/env python3
import sys


def solve(W: int, H: int):
    print("4:3" if W * 3 == H * 4 else "16:9")


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    solve(W, H)


if __name__ == '__main__':
    main()
