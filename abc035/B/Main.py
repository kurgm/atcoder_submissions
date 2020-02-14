#!/usr/bin/env python3
from collections import Counter
import sys


def solve(S: str, T: int):
    c = Counter(S)
    k = abs(c["L"] - c["R"]) + abs(c["U"] - c["D"])
    q = c["?"]
    if T == 1:
        print(k + q)
    elif k > q:
        print(k - q)
    else:
        print((q - k) % 2)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = int(next(tokens))  # type: int
    solve(S, T)


if __name__ == '__main__':
    main()
