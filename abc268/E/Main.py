#!/usr/bin/env python3
import sys
from typing import List

MOD = 4  # type: int


def solve(N: int, p: "List[int]"):
    a = [0] * N
    b = 0
    N2 = N // 2
    for i, pi in enumerate(p):
        s1 = (pi - i) % N
        s2 = (s1 + N2) % N
        s3 = (s1 - N2) % N
        a[s1] += 2
        a[s2] -= 1
        a[s3] -= 1
        if s1 > s2:
            b += 1
        elif s3 > s1:
            b -= 1
    s = 0
    for i, pi in enumerate(p):
        d = (pi - i) % N
        if d <= N2:
            s += d
        else:
            s += (N - d)
    ans = s
    for ai in a:
        b += ai
        s += b
        ans = min(ans, s)

    print(ans)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, p)


if __name__ == '__main__':
    main()
