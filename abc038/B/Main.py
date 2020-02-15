#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(H: "List[int]", W: "List[int]"):
    s1, s2 = list(zip(H, W))
    print(YES if set(s1) & set(s2) else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = [int()] * (2)  # type: "List[int]"
    W = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        H[i] = int(next(tokens))
        W[i] = int(next(tokens))
    solve(H, W)


if __name__ == '__main__':
    main()
