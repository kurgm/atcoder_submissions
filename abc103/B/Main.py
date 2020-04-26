#!/usr/bin/env python3
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str, T: str):
    print(YES if any(
        S == T[i:] + T[:i]
        for i in range(len(T))
    ) else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)


if __name__ == '__main__':
    main()
