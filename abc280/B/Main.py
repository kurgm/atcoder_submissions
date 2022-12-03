#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, S: "List[int]"):
    prev = 0
    A = [0] * N
    for i, Si in enumerate(S):
        A[i] = Si - prev
        prev = Si
    print(*A)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S)


if __name__ == '__main__':
    main()
