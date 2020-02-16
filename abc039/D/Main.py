#!/usr/bin/env python3
from itertools import product
import sys
try:
    from typing import List
except ImportError:
    pass

YES = "possible"  # type: str
NO = "impossible"  # type: str


def solve(H: int, W: int, S: "List[str]"):
    T = [
        "".join(
            "." if any(
                S[i + di][j + dj] == "."
                for di, dj in product((-1, 0, 1), repeat=2)
                if 0 <= i + di < H and 0 <= j + dj < W
            ) else "#"
            for j in range(W)
        )
        for i in range(H)
    ]
    S2 = [
        "".join(
            "#" if any(
                T[i + di][j + dj] == "#"
                for di, dj in product((-1, 0, 1), repeat=2)
                if 0 <= i + di < H and 0 <= j + dj < W
            ) else "."
            for j in range(W)
        )
        for i in range(H)
    ]
    if S == S2:
        print(YES)
        print("\n".join(T))
    else:
        print(NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)


if __name__ == '__main__':
    main()
