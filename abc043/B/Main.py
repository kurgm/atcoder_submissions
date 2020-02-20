#!/usr/bin/env python3
import sys


def solve(s: str):
    z = ""
    for c in s:
        if c == "B":
            z = z[:-1]
        else:
            z += c
    print(z)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    solve(s)


if __name__ == '__main__':
    main()
