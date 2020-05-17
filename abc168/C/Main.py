#!/usr/bin/env python3
import math
import sys


def solve(A: int, B: int, H: int, M: int):
    sa = H * 30.0 + M * 0.5
    la = M * 6.0
    a = abs(sa - la)
    if a > 180:
        a = 360 - a
    print((A * A + B * B - 2 * A * B * math.cos(math.radians(a))) ** 0.5)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(A, B, H, M)


if __name__ == '__main__':
    main()
