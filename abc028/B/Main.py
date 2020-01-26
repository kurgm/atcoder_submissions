#!/usr/bin/env python3
import sys
from collections import Counter


def solve(S: str):
    c = Counter(S)
    print(*(c[ch] for ch in "ABCDEF"))


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
