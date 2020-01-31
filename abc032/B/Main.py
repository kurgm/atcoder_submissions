#!/usr/bin/env python3
import sys


def solve(s: str, k: int):
    print(len({s[i:i+k] for i in range(len(s) - k + 1)}))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    k = int(next(tokens))  # type: int
    solve(s, k)


if __name__ == '__main__':
    main()
