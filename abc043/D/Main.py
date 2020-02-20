#!/usr/bin/env python3
import sys


def solve(s: str):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            print(i + 1, i + 2)
            return
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            print(i + 1, i + 3)
            return
    print(-1, -1)


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
