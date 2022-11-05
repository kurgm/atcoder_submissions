#!/usr/bin/env python3
import sys
from typing import List


def base(s: str) -> int:
    x = 0
    ans = 0
    for si in s:
        if si == "X":
            x += 1
        else:
            sii = int(si)
            ans += x * sii
    return ans


def summ(s: str) -> "tuple[int, int]":
    x = 0
    i = 0
    for si in s:
        if si == "X":
            x += 1
        else:
            i += int(si)
    return x, i


def summkey(summ: "tuple[int, int]") -> float:
    x, i = summ
    if x == 0:
        return float("inf")
    return i / x


def solve(N: int, S: "List[str]"):
    b = sum(base(Si) for Si in S)
    summs = [summ(Si) for Si in S]
    summs.sort(key=summkey)
    ans = b
    x = 0
    for xi, ii in summs:
        ans += x * ii
        x += xi
    print(ans)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()