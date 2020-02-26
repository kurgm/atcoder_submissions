#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    x = 0
    mx = 0
    for Si in S:
        x += 1 if Si == "I" else -1
        mx = max(mx, x)
    print(mx)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)


if __name__ == '__main__':
    main()
