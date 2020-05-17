#!/usr/bin/env python3
import sys


def solve(N: int):
    h = {2, 4, 5, 7, 9}
    p = {0, 1, 6, 8}
    b = {3}
    k = N % 10
    if k in h:
        print("hon")
    if k in p:
        print("pon")
    if k in b:
        print("bon")


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
