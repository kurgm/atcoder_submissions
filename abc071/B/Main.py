#!/usr/bin/env python3
import sys


def solve(S: str):
    a = {chr(c) for c in range(ord("a"), ord("z") + 1)} - set(S)
    print(sorted(a)[0] if a else "None")


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
