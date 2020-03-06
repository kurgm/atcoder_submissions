#!/usr/bin/env python3
import sys


def solve(O: str, E: str):
    print("".join(oi + ei for oi, ei in zip(O, E + " ")).strip())


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    O = next(tokens)  # type: str
    E = next(tokens)  # type: str
    solve(O, E)


if __name__ == '__main__':
    main()
