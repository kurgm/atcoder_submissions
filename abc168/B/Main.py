#!/usr/bin/env python3
import sys


def solve(K: int, S: str):
    print(S if len(S) <= K else S[:K] + "...")


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(K, S)


if __name__ == '__main__':
    main()
