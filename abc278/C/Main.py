#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, Q: int, T: "List[int]", A: "List[int]", B: "List[int]"):
    s: "set[tuple[int, int]]" = set()
    for Ti, Ai, Bi in zip(T, A, B):
        if Ti == 1:
            s.add((Ai, Bi))
        elif Ti == 2:
            s.discard((Ai, Bi))
        else:
            print("Yes" if (Ai, Bi) in s and (Bi, Ai) in s else "No")


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    T = [int() for _ in range(Q)]  # type: "List[int]"
    A = [int() for _ in range(Q)]  # type: "List[int]"
    B = [int() for _ in range(Q)]  # type: "List[int]"
    for i in range(Q):
        T[i] = int(next(tokens))
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, Q, T, A, B)


if __name__ == '__main__':
    main()
