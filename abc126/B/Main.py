#!/usr/bin/env python3
import sys


def solve(S: str):
    d1 = int(S[:2])
    d2 = int(S[2:])
    print({
        (False, False): "NA",
        (False, True): "YYMM",
        (True, False): "MMYY",
        (True, True): "AMBIGUOUS",
    }[1 <= d1 <= 12, 1 <= d2 <= 12])


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
