#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, K: int, s: "List[int]"):
    i = j = 0
    p = 1
    m = 0
    while True:
        while j < N and p * s[j] <= K:
            p *= s[j]
            j += 1
        m = max(m, j - i)
        if j == N:
            break
        p *= s[j]
        j += 1
        while i < j and p > K:
            p //= s[i]
            i += 1
    if p == 0:
        print(N)
    else:
        print(m)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    s = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, s)


if __name__ == '__main__':
    main()
