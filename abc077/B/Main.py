#!/usr/bin/env python3
import sys


def solve(N: int):
    lb = 0
    ub = N + 1
    while lb + 1 < ub:
        m = (lb + ub) // 2
        if m * m > N:
            ub = m
        else:
            lb = m
    print(lb * lb)


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
