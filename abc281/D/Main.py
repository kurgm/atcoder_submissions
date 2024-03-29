#!/usr/bin/env python3
import sys
from typing import List


def solve(N: int, K: int, D: int, a: "List[int]"):
    dp = [[-1] * D for _ in range(K + 1)]
    dp[0][0] = 0
    for ai in a:
        for k in range(K, 0, -1):
            for d in range(D):
                p = dp[k - 1][(d - ai) % D]
                if p >= 0:
                    dp[k][d] = max(dp[k][d], p + ai)

    print(dp[K][0])


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, D, a)


if __name__ == '__main__':
    main()
