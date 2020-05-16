#!/usr/bin/env python3
import sys


def solve(S: str):
    a = S[::2].count("1") + S[1::2].count("0")
    b = S[::2].count("0") + S[1::2].count("1")
    print(min(a, b))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == '__main__':
    main()
