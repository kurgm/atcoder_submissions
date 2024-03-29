#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, M: int, A: "List[int]"):
    dpj = [0] * (N + 1)
    for j in range(M):
        ndpj = [0] * (N + 1)
        for i in range(j + 1, N + 1):
            ndpj[i] = dpj[i - 1] + (j + 1) * A[i - 1]
            if i != j + 1:
                ndpj[i] = max(ndpj[i], ndpj[i - 1])
        dpj = ndpj
    print(dpj[N])


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
