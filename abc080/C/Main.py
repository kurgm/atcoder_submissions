#!/usr/bin/env python3
from itertools import product


try:
    from typing import List
except ImportError:
    pass


def solve(N: int, F: "List[List[int]]", P: "List[List[int]]"):
    print(max(
        sum(
            Pi[sum(ptnj * Fij for ptnj, Fij in zip(ptn, Fi))]
            for Fi, Pi in zip(F, P)
        )
        for ptn in product((0, 1), repeat=10)
        if sum(ptn) != 0
    ))


def main():
    N = int(input())
    F = [
        [int(x) for x in input().split()]
        for _ in range(N)
    ]
    P = [
        [int(x) for x in input().split()]
        for _ in range(N)
    ]
    solve(N, F, P)


if __name__ == '__main__':
    main()
