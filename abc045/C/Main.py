#!/usr/bin/env python3
from itertools import product
import sys


def solve(S: str):
    ans = 0
    for cs in product(("", "+"), repeat=len(S) - 1):
        ans += eval("".join(
            Si + csi for Si, csi in zip(S, cs + ('',))))
    print(ans)


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
