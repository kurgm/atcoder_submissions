#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(A: int, B: int):
    A -= 1
    B -= 1
    print(-(-A // 50 + -B // 50) * 2 + 2, 100)
    while A:
        print("#" * 100)
        n = min(A, 50)
        print(".#" * n + "##" * (50 - n))
        A -= n
    print("#" * 100)
    print("." * 100)
    while B:
        n = min(B, 50)
        print(".#" * n + ".." * (50 - n))
        B -= n
        print("." * 100)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == '__main__':
    main()
