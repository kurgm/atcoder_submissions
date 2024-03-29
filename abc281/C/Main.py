#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, T: int, A: "List[int]"):
    T %= sum(A)
    for i, Ai in enumerate(A):
        if T < Ai:
            print(i + 1, T)
            return
        T -= Ai

    assert False


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, A)


if __name__ == '__main__':
    main()
