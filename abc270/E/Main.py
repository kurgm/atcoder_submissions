#!/usr/bin/env python3
from collections import defaultdict
import sys
from typing import List


def solve(N: int, K: int, A: "List[int]"):
    rev_A_len: "dict[int, int]" = defaultdict(int)
    for Ai in A:
        rev_A_len[Ai] += 1
    n = N
    k = K
    ph = 0
    for h in sorted(rev_A_len):
        dk = n * (h - ph)
        if dk >= k:
            break
        k -= dk
        n -= rev_A_len[h]
        ph = h
    else:
        assert False

    y = ph + k // n
    k %= n
    ans = [0] * N
    for i, Ai in enumerate(A):
        if y >= Ai:
            ans[i] = 0
        elif k > 0:
            ans[i] = Ai - y - 1
            k -= 1
        else:
            ans[i] = Ai - y

    print(*ans)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == '__main__':
    main()