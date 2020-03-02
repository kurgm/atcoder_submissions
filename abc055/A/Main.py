#!/usr/bin/env python3
import sys


def solve(N: int):
    print(N  * 800 - N // 15 * 200)


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
