#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int):
    for i in range(N, -1, -1):
        print(i)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
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
